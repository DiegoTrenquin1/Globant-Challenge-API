--Para este problema separo la query en dos partes
-- 1. Obtengo los datos requeridos.
-- 2. Luego aparte calculo el promedio. 
-- 3. Finalmente haga la consulta general que me obtiene los datos sobre el promedio.

-- Mediante esta forma la query queda mucho mas organizada.

WITH department_hires AS (
    SELECT d.id_department,
           d.name_department,
           COUNT(*) AS hired_c
    FROM public."Employee" e
    JOIN departments d ON e.department_id = d.id_department
    WHERE EXTRACT(YEAR FROM e.date_time) = 2021
    GROUP BY d.id_department, d.name_department
),
avg_hires AS (
    SELECT AVG(hired_c) AS avg_hired
    FROM department_hires
)
SELECT dh.id_department as id,
       dh.name_department as department,
       dh.hired_c AS hired
FROM department_hires dh
JOIN avg_hires a ON dh.hired_c > a.avg_hired
ORDER BY dh.hired_c DESC;