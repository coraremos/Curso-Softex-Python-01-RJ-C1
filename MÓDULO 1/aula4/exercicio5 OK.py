'''
Exercício 5 - Iniciante
Faça um programa que pede ao usuário para digitar uma string e, em seguida, 
imprime a string com todos os caracteres convertidos para maiúsculas e minúsculas alternadamente.
'''

palavra = input('digite uma palavra: ')
resultado = ""

for i, l in enumerate(palavra):
#Percorre cada caractere da palavra, 
# usando enumerate para obter tanto o índice (i) quanto o caractere (l).

    if i % 2 == 0:
        resultado += l.upper()
    else:
        resultado += l.lower()

print(resultado)