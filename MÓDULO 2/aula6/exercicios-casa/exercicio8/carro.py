#Exercício 8: Um Carro que Anda
#Crie uma classe Carro com os atributos modelo e nivel_combustivel (começando com 0).

class Carro:
    def __init__(self, modelo, nivel_combustivel=0) -> None:
        self.modelo = modelo
        self.nivel_combustivel = nivel_combustivel

    def combustivel(self):
        print(f'Você tem {self.nivel_combustivel} litros de combustível no {self.modelo}.')
#1. Crie um método para abastecer(litros) que aumenta o nível de combustível.
    def abastecer(self, litros) -> None:
        self.nivel_combustivel = self.nivel_combustivel + litros
        print(f'Você abasteceu e agora tem {self.nivel_combustivel} litros!')

    def dirigir(self, distancia) -> None:
        if distancia/10 > self.nivel_combustivel:
            print('Não há combustível suficiente pra esse role, abasteça!')
        else:
            self.nivel_combustivel -= distancia/10
            print(f'O carro andou!\nO nível do combustível após o role é de {self.nivel_combustivel}L.')
        
