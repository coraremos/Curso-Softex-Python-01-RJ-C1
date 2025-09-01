'''
Exercício 2 - Iniciante
Faça um programa que solicita dois números e verifica se a multiplicação deles é igual a 100.
'''
header = 'DIGITE DOIS NÚMEROS! E verificarei se a multiplicação é igual a 100.'
print(header)
while True:
    n1 = input('digite o primeiro número: ')
    n2 = input('digite o segundo número: ')
    if n1.isdigit() and n2.isdigit():
        n1 = int(n1)
        n2 = int(n2)
        if (n1*n2) != 100:
            print('a multiplicação desses números não resulta em 100.')
            break
        else:
            print('a multiplicação desses números resulta em 100!')
            break
    else:
        print('dados incorretos, digite números inteiros e positivos:')
print('OBRIGADO POR JOGAR!')
