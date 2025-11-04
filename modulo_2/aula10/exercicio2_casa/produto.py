class Produto:

    def __init__(self, nome:str, preco:float, quantidade_em_estoque:int):
        self.nome = nome
        self._preco = preco
        self._quantidade_em_estoque = quantidade_em_estoque
    
    #um método "getter" para o preço
    def get_preco(self) -> float:
        return self._preco
    
    #um método "setter" para atualizar a quantidade em estoque
    def set_quantidade_em_estoque(self, nova_quantidade: int):
        self._quantidade_em_estoque = nova_quantidade

    def get_quantidade_em_estoque(self) -> int:
        return self._quantidade_em_estoque
    

