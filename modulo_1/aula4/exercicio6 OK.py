'''
Exercício 6 - Iniciante
Escreva um programa que solicita uma palavra e verifica se ela tem a letra 'x'.
'''

l = 'x'
palavra = input('digite uma palavra: ').lower()
if l in palavra:
    print(f'nessa palavra há a letra {l}.')
else:
    print(f'nessa palavra não foi encontrada nenhuma letra {l}')