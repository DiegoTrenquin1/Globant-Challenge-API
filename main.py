import math
from fastapi import FastAPI, HTTPException, UploadFile, File
import models
from database import engine, SessionLocal
import crud
import pandas as pd
import os

app = FastAPI()

#models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

table_names = ["departments", "jobs", "hired_employees"]
BATCH_SIZE = 1000  # Tamaño máximo por lote

@app.post('/data/{table_name}')
async def upload_csv(table_name: str, file: UploadFile = File(...)):
    db = SessionLocal()
    temp_path = None
    total_inserted = 0
    try:
        if table_name not in table_names:
            raise HTTPException(status_code=400, detail="La tabla no existe")
        
        temp_path = f"temp_{file.filename}"
        with open(temp_path, "wb") as buffer:
            buffer.write(await file.read())

        # Leer CSV
        df = pd.read_csv(temp_path, header=None)

        # Asignar columnas y procesar datos según la tabla
        if table_name == "departments":
            df.columns = ["id_department", "name_department"]
            upsert_fn = crud.upsert_departments
            records = df.to_dict(orient="records")

        elif table_name == "jobs":
            df.columns = ["id_job", "title_job"]
            upsert_fn = crud.upsert_jobs
            records = df.to_dict(orient="records")
            
        ##Para esta tabla aplico ciertas transformaciones debido a que vienen nulos y datos con problemas 
        elif table_name == "hired_employees":
            df.columns = ["id_employee", "name_employee", "date_time", "department_id", "job_id"]
            #Convertir a datetime, forzando errores a NaT
            df["date_time"] = pd.to_datetime(df["date_time"], errors="coerce")

            # Reemplazar NaT con None
            df["date_time"] = df["date_time"].apply(lambda x: x if pd.notnull(x) else None)
            df["date_time"] = pd.to_datetime(df["date_time"], errors="coerce", utc=False)

            # Reemplazar todos los NaT por None
            df["date_time"] = df["date_time"].where(pd.notnull(df["date_time"]), None)


            upsert_fn = crud.upsert_employees

            records = []
            for row in df.to_dict(orient="records"):
                # date_time
                if pd.isna(row["date_time"]):
                    row["date_time"] = None
                else:
                    row["date_time"] = row["date_time"].to_pydatetime()
                
                # IDs seguros para BIGINT
                for col in ["id_employee", "department_id", "job_id"]:
                    val = row[col]
                    if pd.isna(val) or str(val).strip() == "" or str(val) == "nan":
                        row[col] = None
                    else:
                        try:
                            x_int = int(float(val))
                            row[col] = x_int
                        except:
                            row[col] = None
                
                records.append(row)


        # Inserción en lotes usando records limpios
        for start in range(0, len(records), BATCH_SIZE):
            batch = records[start:start + BATCH_SIZE]
            try:
                upsert_fn(db, batch)
                total_inserted += len(batch)
            except Exception as e:
                db.rollback()
                print(f"Error insertando batch: {e}")
                continue

        return {"message": f"Inserted {total_inserted} records into {table_name}"}

    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Archivo CSV no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)
        db.close()
