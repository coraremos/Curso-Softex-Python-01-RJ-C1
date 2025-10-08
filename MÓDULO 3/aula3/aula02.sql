CREATE TABLE usuarios(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
)

CREATE TABLE cursos(
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL -- NOT NULL evita que seja inserido valores vazios na tabela
);

CREATE TABLE usuarios_cursos(
    id_usuario INTEGER NOT NULL,
    id_curso INTEGER NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (id_curso) REFERENCES cursos(id)
);

INSERT INTO usuarios(nome) VALUES ('Pedro'), ('Michele'), ('Rafael'), ('Carol');
INSERT INTO cursos(titulo) VALUES ('backend'), ('frontend');
INSERT INTO usuarios_cursos(id_usuario, id_curso) VALUES (1,1), (1,2), (2,1), (3,2);

SELECT * FROM usuarios;
SELECT * FROM cursos;
SELECT * FROM usuarios_cursos;

SELECT U.nome, C.titulo FROM usuarios_cursos AS UC -- U: user C: curso
INNER JOIN usuarios AS U ON UC.id_usuario = U.id -- A ORDEM NÃO IMPORTA! :)
INNER JOIN cursos AS C ON UC.id_curso = C.id;

SELECT usuarios.nome, cursos.titulo FROM usuarios
INNER JOIN usuarios_cursos ON usuarios_cursos.id_usuario = usuarios.id
INNER JOIN cursos ON usuarios_cursos.id_curso = cursos.id

SELECT usuarios.nome, cursos.titulo FROM usuarios_cursos
INNER JOIN usuarios ON usuarios_cursos.id_usuario = usuarios.id
INNER JOIN cursos ON usuarios_cursos.id_curso = cursos.id


SELECT COUNT(*) FROM USUARIOS;
SELECT COUNT(nome) FROM usuarios WHERE nome = 'Carol';

SELECT COUNT(usuarios.nome) AS QTD_ALUNOS, cursos.titulo AS NOME_CURSO 
FROM usuarios_cursos
INNER JOIN usuarios ON usuarios_cursos.id_usuario = usuarios.id
INNER JOIN cursos ON usuarios_cursos.id_curso = cursos.id
GROUP BY cursos.titulo
HAVING COUNT(usuarios.nome) > 1; -- calcular os cursos que tem mais de um aluno/usuario

