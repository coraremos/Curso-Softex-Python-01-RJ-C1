'''
10. Veículos com Herança e Composição (Médio/Difícil)
● Classes: Motor, Roda e Veiculo (base), Carro e Moto (herdam de Veiculo).
● Classe Motor e Roda: As mesmas do Exercício 7.
● Classe Veiculo:
○ Atributos (Composição): motor e rodas (uma lista).
○ Método: __init__(self, numero_de_rodas). O __init__ deve instanciar um Motor e criar
a lista de Rodas com o número especificado.
○ Método: ligar() que chama o método ligar() do motor e depois o método girar() de
todas as rodas.
● Classe Carro:
○ Herança: Carro deve herdar de Veiculo.
○ Método: __init__() que chama super().__init__(4).
● Classe Moto:
○ Herança: Moto deve herdar de Veiculo.
○ Método: __init__() que chama super().__init__(2).
'''