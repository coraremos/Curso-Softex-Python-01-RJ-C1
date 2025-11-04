'''Exercício 1: Filtragem e Análise de Dados de Vendas

Você tem uma lista de vendas, onde cada venda é uma tupla (nome_do_produto, valor,
quantidade).

1. Crie uma nova lista chamada vendas_filtradas contendo apenas as tuplas onde o valor
total da venda (valor * quantidade) é maior que 100.

2. Crie um conjunto com todos os nomes de produtos únicos da lista original.

O que vai entrar:
vendas = [("Teclado", 50, 2), ("Mouse", 25.50, 4), ("Monitor", 300, 1), ("Fone", 45, 1),
("Webcam", 75.20, 2)]
A saída esperada:
Vendas filtradas (valor total > 100):
[('Teclado', 50, 2), ('Mouse', 25.5, 4), ('Monitor', 300, 1), ('Webcam', 75.2, 2)]
Produtos únicos:
{'Monitor', 'Fone', 'Mouse', 'Teclado', 'Webcam'}
'''



vendas = [
    ("Teclado", 50, 2), 
    ("Mouse", 25.50, 4), 
    ("Monitor", 300, 1), 
    ("Fone", 45, 1),
    ("Webcam", 75.20, 2)
]
#(nome_do_produto, valor, quantidade)
vendas_filtradas = []
produtos_unicos = set() #set transforma lista em conjunto, para filtrar itens repetidos!!!

for produto, valor, quantidade in vendas:
    valor_total = valor * quantidade
    if valor_total >= 100:
        vendas_filtradas.append((produto, valor, quantidade)) #criar uma nova lista de tuplas, por isso 2 parenteses
# criar um conjunto só com: (valor*quantidade)>=100
    produtos_unicos.add(produto) #criar um novo CONJUNTO com produtos - produtos_unicos = set()

print("Vendas filtradas (valor total > 100):")
print(vendas_filtradas)

print("\nProdutos únicos:")
print(produtos_unicos)



'''RESOLUÇÃO DO PROF.

vendas = [
    ("Teclado", 50, 2),
    ("Mouse", 25.50, 4),
    ("Monitor", 300, 1),
    ("Fone", 45, 1),
    ("Webcam", 75.20, 2),
]

vendas_filtradas = []
produtos_unicos = set()

for produto, valor, quantidade in vendas:
    valor_total = valor * quantidade
    if valor_total > 100:
        vendas_filtradas.append((produto, valor, quantidade))

    produtos_unicos.add(produto)

print("Vendas filtradas (valor total > 100):")
print(vendas_filtradas)
print("\nProdutos únicos:")
print(produtos_unicos)

'''