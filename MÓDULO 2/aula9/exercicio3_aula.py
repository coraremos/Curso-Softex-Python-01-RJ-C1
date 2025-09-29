'''
3. Segmento de Reta (Fácil/Médio)
● Classes: Ponto e SegmentoDeReta.
● Classe Ponto:
○ Atributos: x e y.
○ Método: __init__(x, y).
● Classe SegmentoDeReta:
○ Atributos (Composição): ponto1 e ponto2, que devem ser instâncias de Ponto.
○ Método: __init__(ponto1, ponto2).

○ Método: calcular_comprimento() que retorna a distância entre os dois pontos.
● Dica: Use o módulo math e a fórmula da distância euclidiana:
(x2−x1)2+(y2−y1)2
'''
import math

class Ponto:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def __str__(self):
        return self.x,self.y

class SegmentoDeReta:
    def __init__(self, ponto1:tuple, ponto2:tuple):
        x1,y1 = ponto1
        x2,y2 = ponto2
        self.ponto1 = Ponto(x1,x2)
        self.ponto2 = Ponto(x2,y2)


    def calcular_comprimento(self):
        comprimento = math.dist(self.ponto1, self.ponto2)
        print(comprimento)

teste = SegmentoDeReta((0,2),(1,3))
teste.calcular_comprimento()





