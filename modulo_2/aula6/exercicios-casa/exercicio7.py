class Retangulo:

    def __init__(self, base:int, altura:int) -> None:
        self.base = base
        self.altura = altura
    
    def calcular_area(self) -> int:
        return self.base * self.altura
    
    def calcular_perimetro(self) -> int:
        return 2 * (self.base + self.altura)

retangulito = Retangulo(5,5)
print(f"A área total do retângulo é {retangulito.calcular_area()}.")
print(f"O perímetro do retângulo é {retangulito.calcular_perimetro()}.")

