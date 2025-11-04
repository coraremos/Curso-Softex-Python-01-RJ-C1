'''
Exercício 4 - Iniciante
Crie um programa que solicita um número e imprime o quadrado desse número.
'''
num = input('insira aqui um número: ')
if num.isdigit():
    num = int(num)
    print(f'o quadrado desse número é: {num*num}')
else:
    print('número inválido! fim do programa')