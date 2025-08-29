#Introdução à Programação com Python

'''
1. Conversor de Moedas Simples (Variáveis e input):
○ Crie um programa que peça ao usuário o valor em reais (float).
○ Calcule o valor equivalente em dólar, sabendo que 1 dólar = R$ 5,00.
○ Imprima o resultado.
'''
#sempre indicar se a str ou float será transformada por numero inteiro fora do input
valor = float(input('insira o valor em reais: R$'))
valor_dolar = valor / 5
print(f'o valor em dolares é: U${valor_dolar:.2f}')
#o valor_dolar pede ':' uma formatação, onde cabe 2 decimais em 'f' de float)

'''
2. Par ou Ímpar (Operadores e if-else):
○ Peça ao usuário para digitar um número inteiro.
○ Use o operador de módulo (%) para verificar se o número é par (o resto da divisão por 2 é 0).
○ Imprima se o número é "Par" ou "Ímpar".
'''
#sempre indicar se a str ou float será transformada por numero inteiro fora do input
numero_inteiro = int(input('digite um numero inteiro: '))
#se o resto da divisão por dois é igual a zero
if (numero_inteiro % 2) == 0:
    print ('é um numero par')
else:
    print ('é um numero impar')

'''
3. Maior de Idade (Aninhamento de if):
○ Peça ao usuário o nome e a idade.
○ Se a idade for maior ou igual a 18, imprima: "Olá, [nome]! Você é maior de idade."
○ Se for menor, imprima: "Olá, [nome]! Você é menor de idade."
'''

nome = input('digite seu nome: ')
idade = int(input('digite sua idade: '))
if idade >= 18:
    print(f'Olá {nome}. Você é maior de idade!')
else:
    print(f'Olá {nome}. Você não é maior de idade!')

'''
4. Sistema de Login Básico (while e break):
○ Defina um nome de usuário e uma senha corretos (ex: admin, 1234).
○ Use um loop while True para pedir ao usuário que digite o nome de usuário e a senha.
○ Se ambos estiverem corretos, imprima "Login bem-sucedido!" e use break para sair do loop.
○ Se estiverem incorretos, imprima "Login inválido. Tente novamente."
'''

while True:
    usuario, senha = 'admin', 1234
    login = input('Digite o seu nome de usuário: ')
    passw = int(input('Agora digite sua senha: '))
    if (usuario, senha) != (login, passw):
        print('Login inválido. Tente novamente.')
    else:
        print('Login bem-sucedido!')
        break

'''5. Calculadora de Média (while e if):
○ Crie um programa que peça notas ao usuário.
○ Use um while para continuar pedindo notas até que o usuário digite -1.
○ Ao final, calcule e imprima a média das notas.'''

notas = []
while True:
    nota = float(input("Digite a nota (ou -1 para sair): "))
    notas.append(nota)
    if nota == -1:
        break
if notas:
    media = sum(notas) / len(notas)
    print(f'a média das notas é: {media}.')
else:
    print("nenhuma nota foi inserida")

'''6. Classificador de Triângulos (if-elif-else):
○ Peça ao usuário para digitar o comprimento de três lados de um triângulo.
○ Use a lógica condicional para classificar o triângulo em:
■ "Equilátero" (todos os lados iguais)
■ "Isósceles" (dois lados iguais)
■ "Escaleno" (todos os lados diferentes)'''

lista_lados = []
while True:
    lado = int(input('insira os três lados do triângulo: '))
    lista_lados.append(lado)
    if len(lista_lados) == 3:
        break
if lista_lados[0] == lista_lados[1] == lista_lados[2]:
    print('esse é um triângulo Equilátero.')
elif lista_lados[0] != lista_lados[1] and lista_lados[0] != lista_lados[2] and lista_lados[1] != lista_lados[2] :
    print('esse é um triângulo Escaleno.')
else:
    print('esse é um triângulo Isósceles.')

'''
7. Contador de Vogais (while):
○ Peça ao usuário para digitar uma palavra.
○ Use um loop while para percorrer a palavra (usando um índice).
○ Conte quantas vogais (a, e, i, o, u) existem na palavra e imprima o total.
'''

palavra = input("Digite uma palavra: ")
indice = 0
vogais = "aeiouAEIOU"
contador_vogais = 0

while indice < len(palavra):
    if palavra[indice] in vogais:
        contador_vogais += 1
    indice += 1

print(f"Total de vogais: {contador_vogais}")

'''
8. Jogo de Adivinhação Melhorado (while, if-elif-else e break):
○ Defina um número secreto.
○ Use um loop while com um contador de tentativas, limitando a 3 tentativas.
○ A cada tentativa, diga se o palpite é maior ou menor que o número secreto.
○ Se o usuário acertar, imprima "Parabéns, você acertou!" e use break.
○ Se as 3 tentativas acabarem, imprima "Você perdeu. O número era [número secreto]."
'''

numero_secreto = 32
tentativas = 0
max_tentativas = 3
while tentativas < max_tentativas:
    numero = int(input(f'Qual é o número secreto? Você terá {tentativas} tentativas:'))
    tentativas += 1
    if numero < numero_secreto:
        print('esse número é menor que o número secreto.')
    elif numero > numero_secreto:
        print('esse número é maior que o número secreto.')
    else:
        print("Parabéns, você acertou o número secreto!")
else:
    print(f'Você perdeu. O número secreto era: {numero_secreto}') 


'''
9. Validação de Dados (while):
○ Peça ao usuário que digite um número entre 1 e 10.
○ Use um while para garantir que a entrada seja válida.
○ Se o número não estiver entre 1 e 10, imprima uma mensagem de erro 
e continue pedindo até que a entrada seja correta.
'''
while True:
    numero = int(input('digite um número entre 1 e 10: '))
    if numero >= 1 and numero <= 10:
        print('número válido!')
        break
    else:
        print('número inválido, tente novamente.')

'''
10. Calculadora de Média com Repetições (while, if-else e break):
○ Crie um programa que permita ao usuário calcular a média de uma turma.
○ Peça a quantidade de alunos. Use um while para garantir que o número seja positivo.
○ Em seguida, use outro while para pedir as notas de cada aluno (uma por uma).
○ Calcule a média final da turma.
'''
while True:
    quantidade_alunos = int(input('digite aqui a quantidade de alunos: '))
    if quantidade_alunos >= 0:
        print(f'a quantidade de alunos é {quantidade_alunos}.')
    else:
        print('quantidade inválida.')
    
    notas = []
    indice = 0
    while indice < quantidade_alunos:
        notas.append(float(input('digite aqui a nota de cada aluno: ')))
        indice += 1
        media_notas = sum(notas) / len(notas)
    print(f'A média das notas dos {quantidade_alunos} alunos é de: {media_notas}.')
    break
