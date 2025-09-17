'''
class Cachorro:

    def __init__(self, nome_do_cao, cor_do_pelo):
        print(f"Um novo cachorro chamado {nome_do_cao} nasceu!")

    def __init__(self, nome_do_cao, cor_do_pelo):
        #o nome DESTE cachorro será:
        self.nome = nome_do_cao
        self.cor = cor_do_pelo

rex = Cachorro("Rex", "Marrom") #INSTANCIANDO A função 'INIT' AUTOMATICAMENTE, DANDO ATRIBUTO AS VARIÁVEIS.

print(rex.cor) #saída: Marrom
'''

#AQUI É UMA VARIÁVEL
class Cachorro:
    def __init__(self, nome_do_cao, cor_do_pelo):
        #o nome DESTE cachorro será:
        self.nome = nome_do_cao
        self.cor = cor_do_pelo


        #AQUI É UMA FUNÇÃO
    #isso é um método/função. uma ação que o objeto pode fazer:
    def latir(self, fala: str) -> None:
        print(f"{self.nome} diz: {fala}")
        #customizou outra ação, 


rex = Cachorro("Rex", "Marrom")
print(f"Um novo cachorro chamado {rex.nome} nasceu!")#a cor será:
print(rex.cor) #saída: Marrom
        
rex.latir("Au AU!") #saída: 'Rex diz: Au au!'


#variável 'nome', variável 'cor', método 'latir'

#chamar variável: 

class Cachorro: #objeto é Cachorro
    #definição inicial para ele mesmo das variáveis nome e cor
    def __init__(self, nome_do_cao, cor_do_pelo):
        #como as variáveis serão chamadas:
        self.nome = nome_do_cao
        #aqui poderá usar 'rex.nome' dentro de print()
        self.cor = cor_do_pelo
        #aqui poderá usar 'rex.cor' dentro de print()

    rex = Cachorro("Rex", "Marrom") #definir características
    print(rex.nome) #saída: Rex
    print(rex.cor) #saída: Marrom

#chamar método:

    #aqui será definido o método "latir" com o valor "fala" e seu formato será em str. 
    # (somente definição, com nenhuma reação imediata.)
    def latir(self, fala: str) -> None:
        # chama a definição através do self.nome, ou seja, nome:"rex", chamando "rex.latir"
        print(f"{self.nome} diz: {fala}")
        #customizou outra ação, 

rex.latir("Au AU!") #saída: 'Rex diz: Au au!'




