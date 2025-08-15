from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'postgresql://db_admin:GlobantTest%402025.%2C@postgres:5432/db_globant'

engine  = create_engine(URL_DATABASE)

SessionLocal =  sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base