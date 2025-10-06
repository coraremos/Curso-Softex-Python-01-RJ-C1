CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY,
    primeiro_nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha INTEGER
);

INSERT INTO usuarios (primeiro_nome,sobrenome,email,senha) VALUES ('João','Silva','joao.silva@email.com', 1234);
INSERT INTO usuarios (primeiro_nome,sobrenome,email,senha) VALUES ('Maria','Dias','maria.dias@email.com', 5678);
INSERT INTO usuarios (primeiro_nome,sobrenome,email,senha) VALUES ('Ruth','Costa','ruth.costa@email.com', 1234);
INSERT INTO usuarios (primeiro_nome,sobrenome,email,senha) VALUES ('Luis','Pinto','maria.dias@email.com', 5678);
INSERT INTO usuarios (primeiro_nome,sobrenome,email,senha) VALUES ('Marcos','Souza','maria.dias@email.com', 1234);

SELECT * FROM usuarios;

CREATE TABLE postagens (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    postagem TEXT NOT NULL,
    id_autor INTEGER
);

INSERT INTO postagens (titulo,postagem,id_autor) VALUES ('Minha primeira postagem','Abcd efgh ijlm', 1);
INSERT INTO postagens (titulo,postagem,id_autor) VALUES ('Minha segunda postagem','Efgh ijlm abcd', 2);
INSERT INTO postagens (titulo,postagem,id_autor) VALUES ('Minha terceira postagem','Efgh ijlm abcd', 3);
INSERT INTO postagens (titulo,postagem,id_autor) VALUES ('Minha quarta postagem','Efgh ijlm abcd', 4);
INSERT INTO postagens (titulo,postagem,id_autor) VALUES ('Minha quinta postagem','Efgh ijlm abcd', 5);

SELECT * FROM postagens;
SELECT titulo, postagem FROM postagens WHERE id_autor = 4;
SELECT email, primeiro_nome FROM usuarios WHERE id = 4;