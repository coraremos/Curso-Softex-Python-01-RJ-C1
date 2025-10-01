from escola import Escola
from estudante import Estudante

escola = Escola()

maria = Estudante("Maria", 15, 6601)
joao = Estudante("João", 14, 6602)

maria.set_materias("Matemática", 10)
maria.set_materias("Inglês", 10)
maria.set_materias("Inglês", 9)

joao.set_materias("Matemática", 9)
joao.set_materias("Inglês", 7)

escola.adicionar_estudante(maria)
escola.adicionar_estudante(joao)
print(escola.lista_estudantes)
escola.mostrar_relatorio()

'''
● Importe as classes Escola e Estudante que você criou. 
● Crie uma instância (um objeto) da sua Escola. 
● Crie pelo menos dois objetos da sua classe Estudante, dando a cada um um nome, idade 
e matrícula. 
● Use os métodos que você criou para: 
○ Adicionar algumas matérias e notas para cada estudante. 
○ Adicionar os estudantes à sua Escola. 
● Chame o método mostrar_relatorio() da sua Escola para ver a mágica acontecer!
'''