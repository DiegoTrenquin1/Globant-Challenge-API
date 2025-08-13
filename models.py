from sqlalchemy import *
from database import Base 

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() 

class Department(Base):
    __tablename__ = 'departments'
    id_department= Column(Integer,primary_key=True)
    name_department= Column(String(255))

class Job(Base):
    __tablename__='jobs'
    id_job= Column(Integer,primary_key=True)
    title_job= Column(String(255))

class Employee(Base):
    __tablename__='Employee'
    id_employee=Column(BigInteger, primary_key=True)
    name_employee= Column(String(255))
    date_time=Column(DateTime)
    department_id=Column(BigInteger)
    job_id= Column(BigInteger)