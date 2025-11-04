#Exercício 10: Um Objeto Dentro de Outro

# Crie duas classes: Motor e Carro.
# 1. A classe Motor terá um atributo potencial.
# 2. A classe Carro terá modelo.
class Motor:
    def __init__(self, potencia:int):
        self.potencia = potencia

class Carro:
    def __init__(self, modelo:str, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)

    def exibir_potencia(self):
        print(f'a potência do seu motor é {self.motor.potencia}')

carro_1 = Carro("Fusca", 100)
carro_1.exibir_potencia()

