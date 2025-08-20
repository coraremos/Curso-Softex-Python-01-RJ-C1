print('hello')

#1

nome1 = input('digite o primeiro nome: ').lower()
nome2 = input('digite o segundo nome: ').lower()
if nome1 == nome2:
    print('nomes iguais')
else:
    print('nomes diferentes')

#2

palavra = input('digite uma palavra: ')
if palavra.startswith('py'):
    print('começa com py')
else:
    print('não começa com py')

#3

texto = input('digite um texto após dar três espaços e complete com três espaços no final: ').strip()
print(f'esse foi o texto:{texto}.')

#4

frase = input('digite uma frase toda em minúsculo: ').title()
print(frase)

#5

frase = input('digite uma frase: ')
palavra = input('qual palavra deseja substituir: ')
palavra_nova = input('por qual nova palavra? ')
frase_nova = frase.replace(palavra,palavra_nova)
print(f'a nova frase é:{frase_nova}')

#6

texto = input('digite um texto: ')
letra = input('digite uma letra: ')
quantidade = texto.count(letra)
print(f'a letra {letra} aparece {quantidade} vezes nesse texto.')

#7

while True:
    numero = input('digite números: ')
    if not numero.isdigit():
        print('você digitou errado, tente novamente:')
    else:
        print('você digitou corretamente')
        break

#8

while True:
    numero_e_letra = input('crie uma senha com somente letras e/ou números: ')
    if not numero_e_letra.isalnum():
        print('você digitou errado, tente novamente:')
    else:
        print('você digitou corretamente')
        break

#9

while True:
    frase = input('digite uma frase e diremos se contém a palavra proibida: ').lower()
    palavra_proibida = 'spoiler'
    if palavra_proibida in frase:
        print('VOCE DIGITOU A PALAVRA PROIBIDA! NO SPOILERS!')
    else:
        print('ufa, não foi dessa vez.')
        break

#11 (treinar a partir da solução dada pelo professor! revisar matéria de index)

senha_forte = input('crie sua senha: ')
while True:
    if len(senha_forte) < 8:
        print('a senha tem caracteres insuficientes')
    else:
        print()
        break

''' TERMINAR DE FAZER O EXERCICIO 11 '''

