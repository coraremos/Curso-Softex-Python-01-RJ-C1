from produto import Produto

class ProdutoEletronico(Produto):
    def __init__(self, nome, preco, quantidade_em_estoque, tempo_garantia_meses):
        super().__init__(nome, preco, quantidade_em_estoque)
        self.tempo_garantia_meses = tempo_garantia_meses
