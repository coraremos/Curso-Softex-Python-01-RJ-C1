'''
    Primeiro, imagine que você esteja codificando um jogo de adivinhação. 
    No código, deverá ser fixado um número inteiro entre 0 e 50, e o jogador deverá tentar adivinhar que número é esse. 
    A cada tentativa errada, o jogo dará uma dica: se o número a ser adivinhado é maior ou menor que aquele que foi digitado. 
    O jogo se encerra apenas quando o jogador adivinhar o valor escondido. 
    Tente realizar este exercício e depois confira abaixo um possível exemplo de solução, que certamente não é a única forma de resolver essa tarefa.'''

# a forma que eu encontrei para fazer:
'''
print('JOGO DE ADIVINHAÇÃO!')

while True:
    num = 42
    ten = input('insira um número entre 0 e 50: ')
    if ten.isdigit():
        ten = int(ten)
        if ten == num:
            print('parabéns, número correto!')
        elif ten < num:
            print('esse número é menor...')
        elif ten > num:
            print('esse número é maior...')
    else:
        print('dado inválido! tente novamente')
'''

# outra forma de fazer
'''
imaginado = 42 #número a adivinhar, escolha o de sua preferência
digitado = 0
print('Você entrou no jogo da adivinhação!')
print('Estou pensando em um número entre 0 e 50...')
while digitado != imaginado:
    digitado = int(input('Escreva um número inteiro com seu palpite: '))
    if digitado > imaginado:
       print('O número que pensei é MENOR! Tente novamente...')
    if digitado < imaginado:
       print('O número que pensei é MAIOR! Tente novamente...')
print('Parabéns! Você adivinhou! Fim de jogo.')
'''
#TABUADA DE 9
'''
numero = 9
for multiplicador in range(1,11):
    print(numero*multiplicador)
'''
#TODAS AS TABUADAS
'''
for n in range(1, 11): #n irá de 1 a 10:
   print('TABUADA DO ', n)
   for v in range(1, 11): #v irá de 1 a 10
     print(n, 'vezes', v, 'é igual a', n*v)
'''
for x in range(5, 9):
    for y in [5, 9]: print('A')