from estudante import Estudante #a classe Estudante vai puxar inclusive a classe Pessoa!

class Escola: #Composição (na escola TEM estudante)

    def __init__(self):
        self.lista_estudantes:list[Estudante] = []

    def adicionar_estudante(self, estudante:Estudante):
        self.lista_estudantes.append(estudante)

    def mostrar_relatorio(self):
        for estudante in self.lista_estudantes:
            print(estudante.get_nome(), estudante.idade, estudante.materias)
    
'''
● Esta classe deve ter uma lista para guardar todos os objetos Estudante. 
● Crie um método adicionar_estudante() para colocar novos estudantes na lista da escola. 
● Crie um método mostrar_relatorio() que percorre a lista de estudantes e imprime todas 
as suas informações: nome, matrícula, e as notas de cada matéria. '''

