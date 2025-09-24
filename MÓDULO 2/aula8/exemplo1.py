class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def som(self):
        print('método da super')

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca #será unicamente Cachorro essa raça

    def som(self):
        print("'Au, Au!!' - método da classe Sub (cachorro)")

class Gato(Animal):
    def __init__(self, nome, idade, especie):
        super().__init__(nome, idade)
        self.especie = especie #será unicamente Cachorro essa raça

cao = Cachorro("Rex", 4 , "Vira_lata")
print(cao.nome)
print(cao.idade)
print(cao.raca)
cao.som()

gato = Gato("Felix", 2, "persa")
print(gato.nome)
print(gato.idade)
print(gato.especie)
gato.som()
