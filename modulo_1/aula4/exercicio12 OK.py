'''
Exercício 12 - Intermediário
Faça um programa que simula a entrada de um sistema. 
O programa deve pedir uma senha e continuar pedindo até que a senha correta ("python123") seja digitada. 
Use um loop while e break.
'''

while True:
    s = "python123"
    senha = input('digite sua senha: ')
    if senha != s:
        print('senha incorreta!')
    else:
        print('login validado')
        break