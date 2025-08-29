''' PT1 '''

#1 Verificador de Comprimento
nome = input("Digite seu nome: ")
print(len(nome))

#2 Verificador de Caractere
palavra = input("Digite uma palavra: ")
if 'a' in palavra:
    print("A letra 'a' está presente na palavra.")
else:
    print("A letra 'a' não está presente na palavra.")

#3 Verificador de Substring
palavra = input('Digite uma palavra: ')
letra = input('Digite uma letra: ')
if letra in palavra:
    print(f'a letra {letra} está na palavra {palavra}!')

#4 Encontrar a Primeira Posição
palavra = input('digite uma palavra: ')
print(palavra.index('e'))
#ou
palavra = input('digite uma palavra: ')
indice = palavra.index('e')
print(indice)

#5 Verificador de Email
while True:
    email = input('digite seu e-mail: ')
    if '@' not in email:
        print('e-mail inválido, tente novamente')
    else:
        print('registrado com sucesso!')
        break

''' PT2 '''

#6 Transformar para Maiúsculas
palavra = input('digite uma palavra em minúsculo: ').upper()
print('você digitou: ', palavra)

#7 Transformar para Minúsculas
palavra = input('digite uma palavra em MAIÚSCULO: ').lower()
print('você digitou: ', palavra)

#8 Remover Espaços
palavra = input('digite uma palavra com espaços no começo e fim da palavra: ').strip()
print('oooO',palavra,'Ooo')

#9 Substituir Caractere
frase = input('digite uma frase: ')
frase2 = frase.replace('a','o')
print(frase2)

#10 Capitalizar a Frase
frase = input('escreva uma frase toda em minúsculo: ').capitalize()
print(frase)

''' PT 3 '''

#11 Validador de Senha(1)
while True:
    senha = input('sua nova senha: ')
    if len(senha) < 8:
        print('senha inválida, tente novamente:')
    else:
        print('senha válida')
        break

#12 Validador de Senha(2)
while True:
    senha = input('nova senha: ')
    if 'senha' in senha:
        print('senha fraca')
    else:
        print('senha forte')
        break

#13 Contador de Vogais

while True:
    palavra = input('digite uma palavra: ')
    vogais_a = int(palavra.count('a'))
    vogais_e = int(palavra.count('e'))
    vogais_i = int(palavra.count('i'))
    vogais_o = int(palavra.count('o'))
    vogais_u = int(palavra.count('u'))
    total_vogais = (vogais_a + vogais_e + vogais_i + vogais_o + vogais_u)
    if total_vogais == 0:
        print('não há vogais, tente novamente')
    else:
        print(f'nessa palavra há {total_vogais} vogais!')
        break

#14 Inversor de Palavras
# Peça ao usuário para digitar uma palavra. 
# Usando len e um laço while, imprima a palavra de trás para frente
palavra = input('Digite uma palavra: ')
indice = len(palavra) - 1
while indice >= 0:
    print(palavra[indice], end="")
    indice -= 1

#15 Caça-Palavras Simples

frase = input('digite uma frase: ').lower()
print(f'essa frase tem {frase.count('a')} letras a')

''' PT 4 '''

#16 Primeiro e Último Caractere
palavra = input('digite uma palavra: ')
if len(palavra) >= 5:
    print(f'a primeira letra é {palavra[0]} e a última é {palavra[-1]}')
else: 
    print('a palavra inteira é:', palavra)

#17 Busca e Substituição 
# Peça ao usuário para digitar uma frase e duas palavras. 
# A primeira palavra é a que será buscada na frase, e a segunda é a que irá substituí-la. 
# Faça a substituição e imprima a nova frase.

frase = input('digite uma frase: ')
palavra1 = input('agora digite uma palavra da frase: ')
palavra2 = input(f'digite uma palavra nova que irá substituir "{palavra1}" na frase: ')
nova_frase = frase.replace(palavra1, palavra2)
print(f'a nova frase é: "{nova_frase}".')

#18 Verificador de Palíndromo
# Peça ao usuário para digitar uma palavra. 
# Verifique se a palavra é um palíndromo (lida da mesma forma de trás para frente). 
# Imprima "É um palíndromo" ou "Não é um palíndromo"

palavra = input('Digite uma palavra: ')
indice = len(palavra) - 1
palavra_invertida = ''

while indice >= 0:
    palavra_invertida += palavra[indice]
    indice -= 1

if palavra == palavra_invertida:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")

#19 Caça-Letras
# Peça ao usuário para digitar uma frase e uma letra. 
# Usando while, encontre todas as posições (índices) onde a letra aparece na frase e imprima-as. 
# Dica: você pode usar a string como uma lista de caracteres

frase = input('Digite uma frase: ')
letra = input('Digite uma letra: ')
indice = 0

print("A letra aparece nas posições:")
while indice < len(frase):
    if frase[indice] == letra:
        print(indice, end=" ")
    indice += 1

#20 Validador de Login Avançado
# Simule um sistema de login. Peça ao usuário para digitar um nome de usuário e uma senha.
#○ O nome de usuário deve ser "admin".
#○ A senha deve ser "12345".
#○ A verificação deve ignorar maiúsculas e minúsculas para o nome de usuário.
#○ Se ambos estiverem corretos, imprima "Acesso concedido". Caso contrário, imprima "Acesso negado".

usuario = 'admin'
senha = '12345'
while True:
    login = input('insira seu usuario: ')
    passw = input('insira sua senha: ')
    if (login == usuario) and (passw == senha):
        print('Acesso concedido.')
        break
    else:
        print('Acesso negado.')