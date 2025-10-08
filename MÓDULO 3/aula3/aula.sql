CREATE Table professores(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE Table alumnos(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    id_professor INTEGER,
    FOREIGN KEY (id_professor) REFERENCES professores(id)
    ON DELETE CASCADE
);
DROP TABLE usuarios_cursos; -- apaga a tabela e tudo dentro
INSERT INTO professores (nome) VALUES ('Anderson');
INSERT INTO professores (nome) VALUES ('Fabricio');

SELECT * FROM professores;

INSERT INTO alumnos(nome, id_professor) VALUES ('João', 1);
INSERT INTO alumnos(nome, id_professor) VALUES ('Maria', 1);
INSERT INTO alumnos(nome, id_professor) VALUES ('Pedro', 2);

SELECT * FROM alumnos

DELETE FROM alumnos WHERE id_professor = 2

SELECT id AS Identificador, nome AS Primeiro_nome FROM alumnos;

SELECT 
    alumnos.nome AS nome_aluno, 
    professores.nome AS nome_professor
FROM
    alumnos
INNER JOIN professores ON alumnos.id_professor = professores.id;

CREATE TABLE alunos_cursos (
    id_aluno INTEGER,
    id_curso INTEGER,
    FOREIGN KEY (id_aluno) REFERENCES alunos(id),
    FOREIGN KEY (id_curso) REFERENCES cursos(id)
)