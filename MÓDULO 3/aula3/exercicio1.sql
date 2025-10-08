DROP TABLE autores;
DROP TABLE livros;

CREATE TABLE autores(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    regionalidade TEXT NOT NULL
)

INSERT INTO autores(nome, regionalidade) VALUES ('Djamila Ribeiro', 'SP'), ('Clarice Lispector', 'PE'), ('Maria Carolina', 'SP')

CREATE TABLE livros(
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    ano_publicacao INTEGER NOT NULL,
    id_autor INTEGER,
    FOREIGN KEY (id_autor) REFERENCES autores(id)
);

INSERT INTO livros(titulo, ano_publicacao, id_autor) VALUES ('Manual Antirracista', 2019, 1), ('Laços de Família', 1975, 2), ('Água Viva', 1973, 2), ('Quarto de Despejo', 1960, 3);

SELECT * FROM autores;
SELECT * FROM livros;

SELECT
    autores.nome AS nome_autor,
    livros.titulo AS titulo_livro
FROM
    livros
INNER JOIN autores ON livros.id_autor = autores.id;

SELECT
    autores.nome AS nome_autor,
    livros.titulo AS titulo_livro
FROM
    livros
INNER JOIN autores ON livros.id_autor = autores.id WHERE autores.regionalidade = 'PE';

SELECT
    autores.nome AS nome_autor,
    livros.titulo AS titulo_livro
FROM
    livros
INNER JOIN autores ON livros.id_autor = autores.id WHERE autores.regionalidade = 'SP';

SELECT COUNT(*) FROM autores;

SELECT COUNT(livros.titulo) AS QTD_LIVROS, autores.nome AS NOME_AUTOR
FROM livros
INNER JOIN autores ON livros.id_autor = autores.id
GROUP BY autores.nome;

--quantos livros cada autor escreveu