'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_primos = []
for i in range(1,11):
    for p in [numeros]:
        if (i > 1) and (i % p) == 0:
            numeros_primos.append(i)
print(numeros_primos)

#ENUNCIADO

Nível 3: Lógica Avançada
Neste nível, os desafios exigem mais de uma lista e combinam diferentes lógicas de controle,
como loops e verificações de pertencimento.
Exercício 3: Filtrando Números Primos
Sua tarefa é criar um programa que percorra uma lista de números e crie uma nova lista
contendo apenas os números que forem primos.
● Entrada: Uma lista de números inteiros.
● Saída: Uma nova lista com os números primos encontrados.
Exemplo:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Resultado Esperado:
[2, 3, 5, 7]
'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primos = []

for numero in numeros:
    eh_primo = True
    if numero < 2:
        eh_primo = False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                eh_primo = False
                break

    if eh_primo:
        primos.append(numero)

print(f"Lista original: {numeros}")
print(f"Números primos na lista: {primos}")
