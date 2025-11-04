CREATE TABLE alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER
);

INSERT INTO alunos (nome,idade) VALUES ('João', 20);
INSERT INTO alunos (nome,idade) VALUES ('Maria', 22);

SELECT * FROM alunos;

SELECT nome,idade FROM alunos;

SELECT * FROM alunos WHERE idade = 20;

UPDATE alunos SET idade = 21 WHERE nome = 'João';

DELETE FROM alunos WHERE nome = 'João'

