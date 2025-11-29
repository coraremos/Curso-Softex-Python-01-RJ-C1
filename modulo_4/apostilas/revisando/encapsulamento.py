""" revisando encapsulamento e decoradores @property e @<nome_da_property>.setter  """

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco

    @property
    def preco(self):
        print("-----------> GETTER com a @property foi chamado!")
        return f"O preço do {self.nome} é R${self._preco:.2f}"
    ''' esse método é executado quando acessamos 'produto.preco' :) '''

    """Para permitir a modificação controlada, usamos um segundo decorador: @<nome_da_property>.setter. 
    Ele "conecta" a lógica do nosso antigo método set_preco à atribuição produto.preco = novo_valor."""

    @preco.setter
    def preco(self, novo_preco):
        ''' executado quando fazemos 'produto.preco = valor' '''
        if isinstance(novo_preco, (int,float)) and novo_preco >= 0:
            self._preco = novo_preco
            print(f"O novo preço do {self.nome} é R${self._preco:.2f}")
        else:
            print("Erro: Forneça um preço numérico e não negativo")

caneta = Produto('bic', 2)
print(caneta.nome)
print(caneta.preco)
caneta.preco = -2
caneta.preco = 4

