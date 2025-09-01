'''
Exercício 13 - Intermediário
Escreva um programa que pede ao usuário para digitar uma frase e, em seguida, 
remove todos os espaços em branco, imprimindo a frase modificada e o seu novo comprimento.
'''

frase = input('digite uma frase: ')
frase_nova = frase.replace(" ", "")
print(f'a frase digitada foi {frase_nova} e o tamanho dela era {len(frase)} mas agora é {len(frase_nova)}')