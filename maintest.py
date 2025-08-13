def upload_data(table_name: str):
    db = SessionLocal()
    print(f"Leyendo el archivo CSV para la tabla {table_name}...")
    try:
        data = read_csv(f"data/{table_name}.csv").to_dict(orient="records")
        print("tabla:",table_name," leida")
        if len(data) > 1000:
            return {"error": "Max 1000 rows per upload"}

        if table_name == "departments":
            data_update = pd.read_csv(f"data/{table_name}.csv", header=None, names=["id_department", "name_department"]).to_dict(orient="records")
            crud.upsert_departments(db, data_update)
            print("Inserto datos en la tabla deparments")
            
        elif table_name == "jobs":
            data_update = pd.read_csv(f"data/{table_name}.csv", header=None, names=["id_job", "title_job"]).to_dict(orient="records")
            crud.upsert_jobs(db, data_update)
            print("Inserto datos en la tabla jobs")

        elif table_name == "hired_employees":
            data_update = pd.read_csv(f"data/{table_name}.csv", header=None, names=["id_employee", "name_employee","deparment_id","job_id"]).to_dict(orient="records")
            crud.insert_employees(db, data_update)
            print("Inserto datos en la tabla employee")

        else:
            return {"error": "La tabla no existe"}
        return {"message": f"Inserted {len(data)} records into {table_name}"}
    except FileNotFoundError:
        print("No se encontro el archivo")
    except Exception as e:
        print("Error al procesar",e)