'''
1. Montando um Carro (Fácil) 
● Classes: Motor e Carro. 
● Classe Motor: 
○ Método: __init__ (sem atributos). 
○ Método: ligar() que imprime "O motor ligou.". 
● Classe Carro: 
○ Atributo (Composição): motor, que deve ser uma instância de Motor. 
○ Método: __init__ que inicializa o atributo motor. 
○ Método: ligar_carro() que chama o método ligar() do seu objeto motor. 
'''

class Motor:
    def __init__(self):
        pass
    def ligar_motor(self):
        print("Motor ligou!")
    def desligar_motor(self):
        print("Motor desligou.")

class Carro:
    def __init__(self):
        #aqui está a composição, o carro "tem um" motor:
        self.motor = Motor() #chama a composição acima, não precisa descrever igual herança no self

    def ligar_carro(self):
        print("O carro está ligando..")
        self.ligar_motor.ligar_carro()
    
    def desligar_carro(self):
        print("O carro está desligando..")
        self.desligar_motor.desligar_carro()

meu_carro = Carro("Fusca")
meu_motor = Motor("rajadao")

meu_carro.ligar_carro()