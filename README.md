# Globant-Challenge-API

Esta aplicación es un FastAPI que permite subir archivos CSV para poblar las tablas departments,
jobs y hired_employees en una base de datos PostgreSQL. El proyecto está dockerizado para facilitar su despliegue.

#Funcionalidades

- Subida de archivos CSV mediante endpoint /data/{table_name}.
- Procesamiento de datos con validaciones y limpieza de columnas.
- Inserción en lotes (batch).
- Conexión con PostgreSQL configurable vía variables de entorno.

## Requisitos

Docker y Docker Compose instalados.
Levantar la aplicación con Docker.

1. Descargar la imagen desde Docker Hub
docker pull dtrenquin/globant-challenge-code-api:latest

2. Crear contenedores con Docker Compose

docker-compose up -d


Esto levantará:

fastapi_app: La API de FastAPI.

postgres: Base de datos PostgreSQL.

pgadmin (opcional): Interfaz gráfica para gestionar la base de datos.

3. Acceder a la aplicación

Swagger UI (documentación automática): http://localhost:8000/docs

PgAdmin: http://localhost:8080 (usuario/contraseña configurados en docker-compose.yml)

4. Subir CSVs

POST al endpoint:

POST /data/{table_name}

Donde {table_name} puede ser:

departments

jobs

hired_employees

### SQL Problems 

En la carpeta SQL podran encontrar la solucion a los dos problemas presentados. 

### Mejoras 

Algunas mejoras que propongo para el proyecto seria:
1. Mejorar la capa de validacion de datos con algun metodo mas controlado o funcion que permita realizar prueba en caso de datos null o na
2. Generar una capa de Front End que sea amigable al usuario y que contenga botones mas didacticos. 
3. Alojar la aplicación en un servicio de hosting web o contenedor en la nube (por ejemplo, AWS, Azure o Heroku) y almacenar los datos en un Data Lake o base de datos centralizada para su posterior procesamiento y análisis.
4. Integrar pipelines de CI/CD para reconstruir automáticamente la imagen Docker y desplegar nuevas versiones cada vez que se realicen cambios en el código, asegurando un flujo de actualización rápido y confiable.

