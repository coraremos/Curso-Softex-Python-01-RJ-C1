'''
Exercício 2: Classe Círculo
Objetivo: Usar um setter para validar dados numéricos e ter métodos que usam a property.
● Requisitos:
1. Crie uma classe Circulo com um atributo protegido _raio.
2. Crie uma @property para raio.
3. Crie um @raio.setter que valide se o valor do raio é um número positivo.
4. Crie um método calcular_area() que use a propriedade self.raio para retornar a área
do círculo (A=π⋅r2).
5. Instancie um círculo, teste a alteração do raio para um valor válido e um inválido, e
imprima a área.

'''
from math import pi
#ou só 'import math' - e quando for usar, escrever math.pi

# 1. Crie uma classe Circulo com um atributo protegido _raio. 
class Circulo:
    def __init__(self, raio:int):
        self._raio = raio

# 2. Crie uma @property para raio.
    @property
    def raio(self) -> int:
        return self._raio

# 3. Crie um @raio.setter que valide se o valor do raio é um número positivo. 
    @raio.setter
    def raio(self, novo_raio) -> None:
        #verificar se o número é positivo E inteiro
        if novo_raio >= 0 and isinstance(novo_raio, int):
            self._raio = novo_raio
        else:
            print('valor incorreto')
    
# 4. Crie um método calcular_area() que use a propriedade self.raio para retornar a área do círculo (A=π⋅r2).
    def calcular_area(self) -> float:
        area = pi * (self.raio ** 2)
        print(f"{area:.2f}")
    
# 5. Instancie um círculo, teste a alteração do raio para um valor válido e um inválido, e imprima a área.
roda = Circulo(2)
print(roda.raio) #puxa da property
roda.calcular_area()
roda.raio = 3
roda.calcular_area()
roda.raio = -1
roda.calcular_area()
