from models import *
from sqlalchemy.orm import sessionmaker

def upsert_departments(db, department_data):
    try:
        for dep_dict in department_data:
            dep_id = dep_dict["id_department"]

            #Buscar si ya existe el registro.
            existing_deparment= db.query(Department).filter_by(id_department=dep_id).first()
            #si existe el registro
            if existing_deparment:
                print("Registro ya existe")
                for key, value in dep_dict.items():
                    setattr(existing_deparment, key, value)
            #Si no existe el registro
            else:
                print("Nuevos registros")
                new_deparment=Department(**dep_dict)
                db.add(new_deparment)
            db.commit()
    except Exception as e:
        print("Error en Insert",e)
        
def upsert_jobs(db,job_data):
    try:
        for job_dict in job_data:
            job_id = job_dict["id_job"]

            #Buscar si ya existe el registro.
            existing_job= db.query(Job).filter_by(id_job=job_id).first()
            #si existe el registro
            if existing_job:
                print("Registro ya existe")
                for key, value in job_dict.items():
                    setattr(existing_job, key, value)
            #Si no existe el registro
            else:
                print("Nuevos registros")
                new_job=Job(**job_dict)
                db.add(new_job)
            db.commit()

    except Exception as e:
        print("Error en Insert",e)

def upsert_employees(db, employee_data):
    try:
        for emp_dict in employee_data:
            emp_id = emp_dict["id_employee"]

            # Buscar si ya existe el registro.
            existing_emp = db.query(Employee).filter_by(id_employee=emp_id).first()

            if existing_emp:
                print(f"Empleado {emp_id} ya existe, actualizando...")
                for key, value in emp_dict.items():
                    setattr(existing_emp, key, value)
            else:
                print(f"Nuevos registros para empleado {emp_id}")
                new_emp = Employee(**emp_dict)
                db.add(new_emp)
            # Muevo commit fuera del else para que se haga siempre (update o insert)
            db.commit()

    except Exception as e:
        print("Error en Insert/Update empleados:", e)

