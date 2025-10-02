from pessoa import Pessoa #aqui eu importo os atributos nome, idade e get_nome

class Estudante(Pessoa): #herança (o Estudante É uma Pessoa)
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.materias = {} 

    def set_materias(self, materia: str, nota:float): 
        aula = self.materias.get(materia) #dentro das minhas materias tem a matéria que eu quero cadastrar?
        if aula:
            aula.append(nota) #se ja existir a materia, adiciona a nota
        else:
            self.materias[materia] = [nota] #se a materia nao existir, adiciona a nova chave e atrela a nova nota

    def __str__(self):
        return self.get_nome() #apenas retorna o valor

'''
● Crie uma classe chamada Estudante que herda (pega emprestado) todas as 
características da classe Pessoa. 
● Adicione um atributo de matrícula a esta classe. 
● Para guardar as notas, use um dicionário, onde a "chave" é o nome da matéria (como 
'Matemática') e o "valor" é uma lista de notas (ex: [9.0, 8.5]). 
● Crie um método "setter" para adicionar notas a uma matéria específica. Um "setter" é 
uma forma de definir ou alterar uma informação dentro do objeto. '''




