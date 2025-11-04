class Loja:

    def __init__(self):
        self.produtos = []
        self.estoque = {}
    
    def adicionar_produto_ao_estoque(self, produto, quantidade):
        self.produtos.append(produto)
        self.estoque[produto.nome] = quantidade
        produto.set_quantidade_em_estoque(quantidade)

    def verificar_estoque_de_produto(self, nome_produto):
        return self.estoque.get(nome_produto, 0)

'''

● Crie um método verificar_estoque_de_produto() que retorna a quantidade em estoque
de um produto específico.'''