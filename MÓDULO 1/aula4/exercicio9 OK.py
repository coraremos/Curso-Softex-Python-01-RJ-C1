'''
Exercício 9 - Iniciante
Escreva um programa que solicita a senha do usuário. A senha deve ter no mínimo 6 caracteres. 
Se não tiver, imprima uma mensagem de erro.
'''
while True:
    senha = input('crie uma senha de seis dígitos: ')
    if len(senha) != 6:
        print('senha inválida!')
    else: 
        print('senha válida')
        break
print('OBRIGADO POR CRIAR SUA SENHA!')