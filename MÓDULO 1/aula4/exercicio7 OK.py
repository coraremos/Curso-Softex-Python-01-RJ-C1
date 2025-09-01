'''
Exercício 7 - Iniciante
Crie um programa que pede ao usuário para digitar um número e usa um loop for para imprimir a tabuada desse número de 1 a 10.
'''
numero = input('digite um número para saber sua tabuada: ')
if numero.isdigit():
    numero = int(numero)
    for multiplicador in range(1,11):
        print(f'o resultado de {numero} vezes {multiplicador} é {numero*multiplicador}.')
else:
    print('caractere inválido!')