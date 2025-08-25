#EXERCICIO 1: simulação de pedido em uma lanchonete

valor_hamburguer = 25.00
cupom_desconto = 'X4780'
desconto = 5.00
titulo = ('Bem-vindos a lanchonete!')
while True:
    produto = input('O que deseja comprar? ')
    if produto == 'hamburguer':
        compra = input(f'Você escolheu {produto}. \n\nVocê tem um cupom? (s/n): ')
        if compra == 's':
            cupom = input('Insira seu cupom: ')
            if cupom != cupom_desconto:
                print('upom inválido.')
            else: 
                print(f'Cupom aplicado! O total da sua compra é de R${valor_hamburguer - desconto:.2f}. Agradecemos a preferência!')
                break
        elif compra == 'n':
            print(f'O valor total da sua compra é de R${valor_hamburguer:.2f}. Agradecemos a preferência!')
            break
        else:
            print('Opção inválida! digite "s" ou "n":')
    else:
        print('Produto não encontrado. Tente novamente!')