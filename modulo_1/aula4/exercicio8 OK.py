'''
Exercício 8 - Iniciante
Faça um programa que solicita uma palavra e imprime a quantidade de vogais (a, e, i, o, u) que ela contém.
'''
count = 0
palavra = input('insira uma palavra: ')
vogais = 'aeiouAEIOU'
for l in palavra:
    if l in vogais:
        count +=1
print(count)
