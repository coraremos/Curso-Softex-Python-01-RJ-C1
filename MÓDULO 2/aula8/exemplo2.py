class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca #será unicamente Cachorro essa raça

    def fazer_som(self):
        print("- Au, Au!!")

#declaração de classe
class Gato(Animal):
    def __init__(self, nome, idade, especie):
        super().__init__(nome, idade)
        self.especie = especie #será unicamente Cachorro essa raça

    def fazer_som(self):
        print('- Miau!')

#criação de objeto
cao = Cachorro("Rex", 4 , "Vira_lata")
gato = Gato("Felix", 2, "persa")

def emitir_som(animal:Animal):
    animal.fazer_som()

emitir_som(cao)
emitir_som(gato)