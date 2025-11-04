import random


class Personagem:
    def __init__(self, nome, vida, ataque, pocoes=0):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.pocoes = pocoes
        self.defendendo = False #dando um valor a uma regra opcional

#ataca o alvo, o segundo personagem, A=self B=alvo, o objeto A(self.nome) está batendo(self.ataque) no objeto B(self.alvo).
    def atacar(self, alvo):
        dano = self.ataque

        if random.random() < 0.2: # calculando 20% de chance de acerto, ou seja, 0.2. se ele gerar um valor menor que 0.2 o alvo é atacado.
            dano *= 2 #aqui calcula o dobro do dano de efeito.
            print(f"Ataque Crítico de {self.nome}!")

        print(f"{self.nome} ataca {alvo.nome} causando {dano} de dano.")
        alvo.receber_dano(dano)

    def defender(self):
        self.defendendo = True
        print(
            (
                f"{self.nome} está defendendo e reduzirá o dano do "
                f"próximo ataque pela metade."
            )
        )

    def receber_dano(self, dano): #aqui será a definição do efeito tanto do "atacar" quanto do "defender"

        if self.defendendo:
            dano = dano // 2
            print(f"{self.nome} defendeu e reduziu o dano para {dano}.")
            self.defendendo = False

        self.vida -= dano #busca o valor da vida e reduz o dano
        self.vida = max(self.vida, 0)

    def usar_pocao(self):
        if self.pocoes > 0:
            cura = 30
            self.vida += cura
            self.pocoes -= 1
            print(
                (
                    f"{self.nome} usou uma poção e recuperou {cura} de vida! "
                    f"Restam {self.pocoes} poções."
                )
            )
        else:
            print(f"{self.nome} não tem poções disponíveis!")

    def esta_vivo(self):
        return self.vida > 0