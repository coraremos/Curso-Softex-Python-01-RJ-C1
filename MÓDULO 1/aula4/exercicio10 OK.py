'''
Exercício 10 - Iniciante
Crie um programa que simula um login. 
Ele deve pedir um nome de usuário (admin) e uma senha (senha123). 
O programa deve permitir apenas uma tentativa.
'''
l = 'admin'
s = 'senha123'

login = input('digite seu login: ')
senha = input('digite sua senha: ')
if login != l or senha != s:
    print('login ou senha incorretos!')
else:
    print('login realizado!')
