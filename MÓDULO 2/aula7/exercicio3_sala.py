'''
Exercício 3: Classe Carro
Objetivo: Usar métodos para interagir com uma propriedade booleana através de seu setter.
● Requisitos:

2. Crie uma @property para ligado.
3. Crie um @ligado.setter que valide se o valor recebido é um booleano (True ou False).
4. Crie um método ligar() que simplesmente faz self.ligado = True.
5. Crie um método desligar() que simplesmente faz self.ligado = False.
6. Instancie um carro, use os métodos ligar() e desligar() e imprima o status da
propriedade ligado após cada ação
'''

#1. Crie uma classe Carro com o atributo protegido _ligado (booleano).
class Carro:
    def __init__(self, ligado:bool):
        self._ligado