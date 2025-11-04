class Produto:

    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco
    
    def apresentar(self):
        print(f"O produto '{self.nome}' está custando R${self.preco:.2f} (valor unitário).")
        return
