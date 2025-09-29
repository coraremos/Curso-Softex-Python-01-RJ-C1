'''
8. Carrinho de Compras (Médio)
● Classes: Produto, ItemDeCompra e CarrinhoDeCompras.
● Classe Produto:
○ Atributos: nome e preco.
○ Método: __init__(nome, preco).
● Classe ItemDeCompra:
○ Atributos (Composição): produto (um objeto Produto) e quantidade.
○ Método: __init__(produto, quantidade).
● Classe CarrinhoDeCompras:
○ Atributo (Composição): itens, que deve ser uma lista vazia.
○ Método: __init__ que inicializa a lista itens.
○ Método: adicionar_item(produto, quantidade) que cria um objeto ItemDeCompra e o
adiciona na lista.
○ Método: calcular_total() que itera sobre a lista itens e retorna a soma total dos
preços (preço do produto * quantidade).
'''