SET lc_monetary = 'pt_BR';

-- Selecionando todas as colunas
SELECT * FROM employees;

-- Selecionando colunas em específico
SELECT name, age FROM employees;

-- Definindo um limite para a consulta
SELECT * FROM employees LIMIT 5;

-- Definindo um início para a consulta
SELECT * FROM employees LIMIT 5 OFFSET 3;

-- Selecionando os dados com condições 
SELECT * FROM employees WHERE age > 30;

-- Between - Intervalo de valores
SELECT * FROM employees WHERE age BETWEEN 20 AND 25;

-- Casting -> Conversão de tipo de dado
SELECT * FROM employees WHERE salary BETWEEN 'R$ 3000' AND 'R$ 7000'

SELECT * FROM employees WHERE CAST (salary AS numeric) BETWEEN 3000 AND 7000;

SELECT * FROM employees WHERE salary:: numeric BETWEEN 3000 AND 7000;

-- Operador IN 
SELECT * FROM employees WHERE age IN (27, 29, 41);

-- Operador LIKE 
SELECT * FROM employees WHERE name LIKE '%ig%';

SELECT * FROM employees WHERE name ILIKE '%ig%';

SELECT * FROM employees WHERE name ILIKE '%re__';

-- INNER JOIN - Seleciona a intersecção entre as duas tabelas
SELECT employees.name, departments.name
FROM employees
INNER JOIN departments 
ON employees.department_id = departments.id

-- Definindo apelidos para as colunas
SELECT employees.name "Nome do funcionário", departments.name "Nome do departamento"
FROM employees
INNER JOIN departments 
ON employees.department_id = departments.id

-- Definindo apelidos para as tabelas
SELECT e.name "Nome do funcionário", d.name "Nome do departamento"
FROM employees e 
INNER JOIN departments d
ON e.department_id = d.id;

-- LEFT JOIN
SELECT e.name funcionário, d.name departamento
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.id;

-- RIGHT JOIN
SELECT e.name funcionário, d.name departamento
FROM employees e
RIGHT JOIN departments d
ON e.department_id = d.id;

-- FULL JOIN 
SELECT e.name funcionário, d.name departamento
FROM employees e
FULL JOIN departments d
ON e.department_id = d.id;

-- Função Agregadoras 
-- COUNT - Conta as ocorrências
SELECT COUNT (*) FROM employees;

SELECT COUNT (*) FROM employees WHERE salary::numeric > 3000;

-- MAX - Maior valor
SELECT MAX(salary) FROM employees;

-- MIN - Menor valor
SELECT MIN(salary) FROM employees;

-- SUM - Soma dos valores
SELECT SUM(salary) FROM employees;

-- AVG - Média dos valores
SELECT AVG(salary::numeric) FROM employees;

-- ROUND - Arrendondar casas decimais
SELECT ROUND (AVG(salary::numeric), 2) FROM employees;

-- GROUP BY - Agrupar colunas
SELECT department_id "ID do departamento", COUNT(*) "Quantidade de funcionários"
FROM employees
GROUP BY 1;

-- COALESCE - Verifica se a coluna possui valor, caso não possuir, mostra um valor padrão
SELECT
	COALESCE(department_id::text, 'Funcionários sem departamento') "ID do departamento",
	COUNT(*) "Quantidade de funcionários"
FROM employees
GROUP BY 1;

-- Com LEFT JOIN 
SELECT
	COALESCE(d.name, 'Funcionários sem departamento') "ID do departamento",
	COUNT(*) "Quantidade de funcionários"
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.id
GROUP BY 1;