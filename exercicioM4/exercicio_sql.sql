DROP TABLE IF EXISTS Itens_Pedido;
DROP TABLE IF EXISTS Pedidos;
DROP TABLE IF EXISTS Produtos;
DROP TABLE IF EXISTS Clientes;

CREATE TABLE Clientes (
    id SERIAL PRIMARY KEY, 
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE Produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL, 
    estoque INTEGER NOT NULL
);

CREATE TABLE Pedidos (
    id SERIAL PRIMARY KEY,
    data_compra TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10, 2),
    id_cliente INTEGER NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id)
);

CREATE TABLE Itens_Pedido (
    id SERIAL PRIMARY KEY,
    id_pedido INTEGER NOT NULL,
    id_produto INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES Pedidos(id),
    FOREIGN KEY (id_produto) REFERENCES Produtos(id)
);

INSERT INTO Clientes (nome, email) VALUES 
('João', 'joao@email.com'),
('Maria', 'maria@email.com'),
('Ana', 'ana@email.com');

INSERT INTO Produtos (nome, preco, estoque) VALUES 
('Teclado Mecânico', 150.00, 50),
('Mouse Gamer', 80.00, 30),
('Monitor 24pol', 850.90, 10);

INSERT INTO Pedidos (id_cliente, total, data_compra) VALUES 
(2, 310.00, '2023-10-25 14:30:00');

INSERT INTO Itens_Pedido (id_pedido, id_produto, quantidade) VALUES (1, 1, 1);
INSERT INTO Itens_Pedido (id_pedido, id_produto, quantidade) VALUES (1, 2, 2);

SELECT nome, preco 
FROM Produtos 
WHERE preco > 100.00;

SELECT 
    c.nome AS Nome_Cliente, 
    p.id AS ID_Pedido, 
    p.data_compra 
FROM Pedidos p
JOIN Clientes c ON p.id_cliente = c.id
WHERE c.nome = 'Maria';

UPDATE Produtos 
SET preco = preco * 1.10 
WHERE nome = 'Mouse Gamer';

UPDATE Produtos 
SET estoque = estoque - 2 
WHERE nome = 'Mouse Gamer';

DELETE FROM Clientes 
WHERE nome = 'João';

DELETE FROM Itens_Pedido 
WHERE id_pedido = 1 AND id_produto = 1;