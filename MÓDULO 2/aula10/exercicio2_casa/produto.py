class Produto:

    def __init__(self, nome:str, preco:float, quantidade_em_estoque:int):
        self.nome = nome
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque
    
    #um método "getter" para o preço
    def get_preco(self):
        return self.get_preco
    
    #um método "setter" para atualizar a quantidade em estoque
    def set_quantidade_em_estoque(self):
        return self.set_quantidade_em_estoque
