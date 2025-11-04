import random

# RANDOM, UNIFORN, RANDRANGE, RANDIT
print(random.random()) #irá gerar valores entre 0.0 até 0.1
print(random.uniform(1,10)) #parede range, gerando valor decimal de 1 a 10 em float
print(random.randrange(0,5)) #não inclui o último número
print(random.randint(1,10)) #gera valores inteiros, do mínimo ao máximo(pode sair 10)

# CHOICE
cores = ['verde', 'vermelha', 'azul']
print(random.choice(cores)) #escolhe uma opção dentro de uma fonte pré definida

# CHOICES
numeros = [1,2,3,4,5,6,7,8,9,10]
print(random.choices(numeros, k=5)) #gera uma lista com números (quantidade = k) com risco de haver repetições

print(random.sample(numeros, k=5)) #gera uma lista onde os números não se repetem

#SHUFFLE
cartas_de_um_baralho = ['carta1','carta2','carta3','carta4','carta5']
random.shuffle(cartas_de_um_baralho)
print(cartas_de_um_baralho) #altera a lista inicial diretamente
