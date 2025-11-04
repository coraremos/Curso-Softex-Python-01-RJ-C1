'''
Exercício 3 - Iniciante
Escreva um programa que pede ao usuário para digitar uma cor. 
O programa deve verificar se a cor é "vermelho", "azul" ou "amarelo" e imprimir "Cor primária!" se a condição for verdadeira.
'''
header = 'BEM VINDOS A LOJA DE CORES DA CORAR!'
red = 'vermelho'
blu = 'azul'
yel = 'amarelo'
print(header)
while True:
    cor = input('consulte aqui uma cor: ').lower()
    if cor == red or cor == blu or cor == yel:
        print(f'nós temos a cor {cor}!')
        break
    else:
        print('não temos essa cor, tente de novo!')
print('CORAR AGRADECE!')