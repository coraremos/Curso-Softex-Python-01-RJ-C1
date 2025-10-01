class Pessoa:
    def __init__(self,nome:str,idade:int):
        self.nome = nome
        self.idade = idade
    
    def get_nome(self): #get é usado para evitar erros quando buscar chaves sem valores
        return self.nome 
    
'''
● Crie uma classe (o nosso molde) chamada Pessoa. 
● Essa classe deve ter um nome e uma idade. 
● Para garantir que as informações sejam acessadas e modificadas de forma organizada, 
implemente um método "getter" para o nome. Um "getter" é uma forma de obter a informação de um objeto. '''