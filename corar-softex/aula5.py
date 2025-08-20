'''palavra = 'teste'

for letra in palavra:
    print(letra)
'''

'''
palavra = 'teste'
#até o número cinco, ou se quiser pegar um período específico especificar range(início, fim, intervalo)
for letra in range(5):
    print(letra)
'''

#    ou

'''
palavra = 'teste'

for letra in range(len(palavra)):
    print(palavra[letra])
'''

#se eu preciso que ele interrompa em determinado valor, uso FOR, caso não, uso WHILE.

#1 tabuada simples: crie um programa que solicita ao usuário um número inteiro. 
#Em seguida use um loop for para imprimir a tabuada desse numero de 1 a 10

numero = int(input('digite aqui um número inteiro: '))
#cria uma variável "multiplicador" para entender a lista de numeros de 1 a 10
for multiplicador in range(1,11):
    #pede a multiplicação (por 1, por 2, por 3... até 10 do número inicial)
    print(numero*multiplicador)

#OU

numero = int(input('digite um numero: '))
for i in range(1,11):
    print(f"{numero} x {i} = {numero*i}")

#2
palavra = ABELHA
vogais = 'aeiouAEIOU'
contador = 0
# a nova variável letra vai ler letra por letra da palavra escrita
# / se a letra estiver dentro das vogais destacadas
# / contar a quantidade encontrada 
# (ENCONTROU 1? VAI SOMAR MAIS UM. ENCONTROU MAIS UM? VAI SOMAR MAIS UM, ENCONTROU MAIS UM, VAI SOMAR MAIS DOIS) mais ela mesma
for letra in palavra:
#indentar outras condições da primeira condição é ok
    if letra in vogais:
        contador += 1 #
print(f'essa palavra possui {contador} vogais')

GIT

git --version
git init
git checkout -b main
git branch
git status
git commit -m "anotações e exercícios realizados na aula 5"  
#(comment = commit)

git config user.name "corarwho"
git config user.email "carol.vrcosta@gmail.com"
git remote add origin https://github.com/corarwho/seu-novo-repo #link criado a partir de um novo repo no gitHub
