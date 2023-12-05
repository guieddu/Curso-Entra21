-- 2) a)
SELECT SUM(quantity_in_stock) "Produtos em estoque" FROM products;

-- b)
SELECT ROUND(AVG(price::numeric), 2)
FROM products;

-- c)
SELECT 
	product "Produto", 
	price "Preço"
FROM products
ORDER BY 2 DESC
LIMIT 1;

-- d)
SELECT 
	product "Produto", 
	price "Preço"
FROM products
ORDER BY 2
LIMIT 1;

-- e)
SELECT 
	product "Produto", price * quantity_in_stock "Valor total do estoque" 
FROM products;

-- f)
SELECT SUM(contagem) "Soma total"
FROM (
	SELECT COUNT(*) "contagem"
	FROM products
	GROUP BY quantity_in_stock
	HAVING quantity_in_stock < 20
);

-- g)
SELECT 
	product "Produto", price * quantity_in_stock "Valor total do estoque"
FROM products
ORDER BY 2 DESC
LIMIT 1;
