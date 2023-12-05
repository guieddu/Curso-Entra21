-- 3) a)
SELECT
	e.name "Colaborador",
	e.role "Cargo",
	d.name "Departamento"
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;

-- b)
SELECT
	e.name "Colaborador",
	e.role "Cargo",
	e.salary "Salário"
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE d.name = 'Vendas';

-- c)
SELECT
	e.name "Colaborador",
	e.role "Cargo",
	e.salary "Salário"
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE salary::numeric > 3500 AND d.name = 'Vendas';

-- d)
SELECT 
    e.employee_name,
    e.job_title,
    e.salary,
    p.project_name
FROM 
    employees e
JOIN 
    projects p ON e.project_id = p.project_id;
	
-- e)
SELECT 
	SUM(salary) "Gasto total com salários"
FROM employees;

-- f)
SELECT 
	SUM(e.salary) Soma salários, 
	d.name Departamento
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id
GROUP BY d.name;

-- g)
SELECT
	d.name "Departamento",
	MAX(e.salary) "Maior salário"
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
GROUP BY d.name;