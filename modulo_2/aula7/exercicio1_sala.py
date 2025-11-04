'''
Exercício 1: Classe Pessoa
Objetivo: Criar uma classe com validações simples nos setters para tipo e valor.
● Requisitos:


6. No __init__, use os setters para atribuir os valores iniciais (ex: self.nome = nome).
7. Instancie um objeto Pessoa com dados válidos e depois tente alterar nome para um
valor vazio e idade para um valor negativo para testar as validações.
'''
#1. Crie uma classe Pessoa com os atributos protegidos _nome e _idade.
class Persona:
    def __init__(self, nome:str, idade:int):
        self._nome = nome 
        self._idade = idade

    #2. Crie uma @property para nome.
    @property
    def nome(self):
        return self._nome
    
    #3. Crie um @nome.setter que valide se o valor é uma string e não está vazio.
    @nome.setter
    def nome(self, novo_nome:str):
        #isinstance verifica se o primeiro parametro é do tipo do segundo
        # 'and novo_nome' identifica se há valores dentro dele.
        if isinstance(novo_nome, str) and novo_nome:
            self._nome = novo_nome
        else:
            print('nome incorreto!')
    
    #4. Crie uma @property para idade.
    @property
    def idade(self):
        return self._idade
    
    #5. Crie um @idade.setter que valide se a idade é um número inteiro e positivo.
    @idade.setter
    def idade(self, nova_idade):
        if isinstance(nova_idade, int) and nova_idade > 0:
            self._idade = nova_idade
        else:
            print('Nova idade deve ser um inteiro positivo!')
    
aluno = Persona ("Cora", 30)
print(aluno.nome)
print(aluno.idade)

aluno.nome = "Maria"
print(aluno.nome)
aluno.idade = 20
print(aluno.idade)

