class Cachorro:
    def __init__(self, nome: str, cor: str) -> None:
        self.nome = nome
        self.cor = cor
    
    def latir(self, fala: str) -> None:
        print(f"{self.nome} diz: {fala}")

meu_cachorro = Cachorro("Rex", "preto")

#variável 'nome', variável 'cor', método 'latir'
print(meu_cachorro.nome)
print(meu_cachorro.cor)

#digitando ponto, aparecem sugestões. Ex.: "". ao digitar ponto após as aspas aparecem as sugestões para str

#nome e cor são atributos (variáveis) da classe (objeto) Cachorro
#por isso, não são chamadas com parênteses: () !!! 

meu_cachorro.latir("Au au!")

