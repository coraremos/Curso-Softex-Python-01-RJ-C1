'''
Exercício 2: Comparação de Estoque

Você tem o inventário de uma loja em duas listas de tuplas. Cada tupla representa um produto:
(nome_do_produto, id)

● estoque_principal: Produtos disponíveis na loja.
● estoque_online: Produtos disponíveis no site.

Usando conjuntos, descubra e imprima:
1. Os produtos que estão disponíveis tanto na loja física quanto no site.
2. Os produtos que estão apenas na loja física.
3. Os produtos que estão apenas no site.

O que vai entrar:

estoque_principal = [("Camiseta", 101), ("Calça", 102), ("Boné", 103), ("Tênis", 104)]
estoque_online = [("Boné", 103), ("Camisa Polo", 105), ("Calça", 102), ("Chinelo", 106)]

A saída esperada:

Produtos disponíveis na loja e no site:
{('Boné', 103), ('Calça', 102)}
Produtos disponíveis apenas na loja física:
{('Camiseta', 101), ('Tênis', 104)}
Produtos disponíveis apenas no site:
{('Camisa Polo', 105), ('Chinelo', 106)}
'''

estoque_principal = [
    ("Camiseta", 101), 
    ("Calça", 102), 
    ("Boné", 103), 
    ("Tênis", 104)
]

estoque_online = [
    ("Boné", 103), 
    ("Camisa Polo", 105), 
    ("Calça", 102), 
    ("Chinelo", 106)
]

cjt_estoque = set(estoque_principal)
cjt_online = set(estoque_online)

#o que tem no principal que também tem no online
disponiveis_ambos = cjt_estoque.intersection(cjt_online)

#diferença do que tem no estoque mas não está na loja
disponiveis_loja = cjt_estoque.difference(cjt_online)

#diferença do que tem na loja mas não está no estoque
disponiveis_site = cjt_online.difference(cjt_estoque)


print(f'Produtos disponíveis na loja e no site: \n{disponiveis_ambos}')
print(f'\nProdutos disponíveis apenas na loja online: \n{disponiveis_site}')
print(f'\nProdutos disponíveis apenas na loja física: \n{disponiveis_loja}')