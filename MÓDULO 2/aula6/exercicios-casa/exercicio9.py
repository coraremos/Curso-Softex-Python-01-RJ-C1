#Exercício 9: Atributo da Classe (Funcionários da Empresa)

# Crie uma classe Funcionario. Cada funcionário terá nome e salário (atributos de instância). 
class Funcionario:
    # Agora, crie um atributo de classe chamado percentual_bonus, com o valor 1.10 (representando 10% de bônus).
    percentual_bonus = 1.10

    def __init__(self, nome:str, salario:float) -> None:
        self.nome = nome
        self.salario = salario
    
    # Crie um método aplicar_bonus que multiplica o salário do funcionário pelo percentual_bonus da classe. 
    def aplicar_bonus(self) -> float:
        return self.salario * self.percentual_bonus
        
# Crie dois funcionários com salários diferentes, aplique o bônus e veja o resultado.
funcionario1 = Funcionario('Maria', 1500.00)
funcionario2 = Funcionario('João', 2000.00)

print(f"{funcionario1.aplicar_bonus():.2f}")
print(f"{funcionario2.aplicar_bonus():.2f}")

