#1. Nível Fácil: Registro de Pessoas

#Crie uma classe base Pessoa com um construtor que recebe nome e idade.
class Pessoa:
    def __init__(self, nome:str, idade:int) -> None:
        self._nome = nome
        self._idade = idade
    
    #Adicione um método apresentar() que imprime uma frase com o nome e a idade da pessoa.
    def apresentar(self) -> None:
        return(f"Olá, meu nome é {self._nome}, minha idade é {self._idade}")

#Em seguida, crie uma classe Estudante que herda de Pessoa.
class Estudante(Pessoa):
    #O construtor de Estudante deve chamar o construtor da classe pai e adicionar um atributo para o curso.
    def __init__(self, nome:str, idade:int, curso:str) -> None:
        super().__init__(nome, idade)
        self._curso= curso

    #A classe Estudante deve sobrescrever o método apresentar() para incluir o curso na frase.
    def apresentar(self) -> None:
        return(f"e meu curso é {self._curso}.")

pessoa = Estudante("Cora", 32, "Python")

#Por fim, crie uma lista com um objeto Pessoa e um objeto Estudante. 
lista = [Pessoa.apresentar(pessoa)] 
lista_estudante = [Estudante.apresentar(pessoa)]
#Itere sobre a lista e chame o método apresentar() para cada item, demonstrando o polimorfismo.

for item in lista:
    print(item, end=" ")

