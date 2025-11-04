from produto import Produto

class ProdutoEletronico(Produto):
    def __init__(self, nome:str, preco:float, quantidade_em_estoque:int, tempo_garantia_meses:int):
        super().__init__(nome, preco, quantidade_em_estoque)
        self.tempo_garantia_meses = tempo_garantia_meses
