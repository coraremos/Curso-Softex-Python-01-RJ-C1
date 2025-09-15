def solicitar_forma_pagamento() -> str:
    '''solicitar e retornar a forma de pagamento escolhida'''
    while True:
        pagamento = input('Escolha a forma de pagamento (1-Dinheiro, 2-Cartão):')
        if pagamento == "1":
            return "Dinheiro"
        elif pagamento == "2":
            return "Cartão"
        else:
            print('Forma de pagamento inválida')