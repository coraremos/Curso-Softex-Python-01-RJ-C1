'''
Exercício 11 - Intermediário
Crie um programa que solicita ao usuário um número e, em seguida, usa um loop for para
imprimir todos os números pares de 2 até o número digitado.
'''

numero = input('digite um número: ')
if numero.isdigit:
    numero = int(numero)
    for n in range(0, (numero+1), 2):
        print(n, end=" ")