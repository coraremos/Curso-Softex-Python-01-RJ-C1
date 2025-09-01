'''
Exercício 1 - Iniciante
Crie um programa que pede ao usuário para digitar sua idade. 
Se a idade for maior ou igual a 18, imprima "Você é maior de idade.". 
Caso contrário, imprima "Você é menor de idade.".
'''

while True:
    idade = input('digite a sua idade: ')
    if idade.isdigit():
        idade = int(idade)
        if idade >= 18:
            print('você é maior de idade!')
            break
        elif idade < 18:
            print('você é menor de idade.')
            break
    else:
        print('o valor digitado é inválido.')