-- 1) a) 
SELECT title, author FROM books;

-- b)
SELECT title "Título do Livro"
FROM books
WHERE author = 'Henry Davis';

-- c)
SELECT 
	title, 
	author, 
	release_year
FROM books
WHERE release_year < 1900;

-- d)
SELECT *
FROM books 
WHERE title LIKE 'O%';

-- e)
SELECT
	title "Título do Livro",
	author "Autor do Autor"
FROM books
WHERE release_year > 1950
ORDER BY release_year;

-- f)
SELECT 
	COUNT(*) "Quantidade de livros"
FROM books;

-- g)
SELECT author, COUNT(*) AS num_books
FROM books
GROUP BY author
ORDER BY num_books DESC
LIMIT 1;

-- h)
SELECT * 
FROM books
ORDER BY release_year;

-- i)
SELECT title
FROM books 
ORDER BY release_year  
LIMIT 1;

-- j)
SELECT title
FROM books 
ORDER BY release_year DESC  
LIMIT 1;

-- k)
SELECT 
	title, 
	author 
FROM books
ORDER BY id DESC
LIMIT 3;
