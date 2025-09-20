#criar uma classe, definir o __init__, criar atributos e instanciar objetos.

#Crie uma classe chamada Pessoa. No "registro de nascimento" (__init__), toda pessoa deve ter um nome e uma idade.

class Pessoa:
    
    def __init__(self, nome: str, idade: int, comendo=False, falando=False) -> None:
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f"{self.nome} não pode falar enquanto estiver comendo")
            return
        
        if self.falando:
            print(f"{self.nome} já está falando")
            return
        
        print(f"{self.nome} está falando...\n '{assunto}'")
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return
        
        print(f"{self.nome} parou de falar.")
        self.falando = False

    def comer(self, alimento):

        if self.comendo:
            print(f"{self.nome} já está comendo!")
            return
        
        if self.falando:
            print(f"{self.nome} não pode comer enquanto estiver falando")
            return

        print(f"{self.nome} está comento {alimento}.")
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        
        print(f'{self.nome} parou de comer.')
        self.comendo = False