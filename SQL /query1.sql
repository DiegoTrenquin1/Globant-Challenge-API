--Utilizo la funcion QUARTER para devolver el numero de trimestre segun el 
--date_time

--Se puede utilizar la funcion CASE WHEN o bien EXTRACT (Para casos mas simples 
-- utilice filter ya que filter directamente dentro de la columna date_time

--Lo demas son simples join de las tablas indicadas. 

SELECT 
d.name_department AS departments,
j.title_job AS job,
COUNT(*) FILTER ( WHERE EXTRACT(QUARTER FROM e.date_time) = 1) AS Q1,
COUNT(*) FILTER ( WHERE EXTRACT(QUARTER FROM e.date_time) = 2) AS Q2,
COUNT(*) FILTER ( WHERE EXTRACT(QUARTER FROM e.date_time) = 3) AS Q3,
COUNT(*) FILTER ( WHERE EXTRACT(QUARTER FROM e.date_time) = 4) AS Q4
FROM public."Employee" e
JOIN departments d ON e.department_id = d.id_department
JOIN jobs j ON e.job_id  = j.id_job
WHERE EXTRACT(YEAR FROM e.date_time) = 2021
GROUP BY d.name_department, j.title_job
ORDER BY d.name_department, j.title_job;