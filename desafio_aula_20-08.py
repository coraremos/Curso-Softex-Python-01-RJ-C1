'''
comércio: Padaria Softex
1- O programa tem que rodar em loop infinito até ser parado
2- Cliente deve pedir um tipo de pão (pão francês, pão doce, pão de forma)
3- Cada pão terá uma quantidade de estoque
4- Cada pão terá um preço
5- Pedir a forma de pagamento (dinheiro ou cartão)
6- Forma de entrega
7- Pedir dados do cliente (se for entregar nome e endereço, se for buscar só o nome)
8- valor do frete por bairro
9- nome do atendente
10- codigo de entrega
'''

''' minha tentativa
while True:
    pedido = input('Olá, somos a Padaria Softex. Você deseja iniciar um pedido? (s/n): ')
    if pedido == 's':
       pao = input('Então vamos começar! Temos as oções: \n1-Francês,\n2-Pão Doce,\n3-Pão de forma,\n4-Australiano.\n Digite o número do pão que você deseja: ' )
       if pao == '1':
         print('Você escolheu Pão Francês!')
    elif pedido == 'n':
      print('Agradecemos a sua visita! Ficamos a disposição.')
      break
    else: 
      print('Resposta inválida')
'''

#fazendo junto com o professor:

#banco de dados, com todos os valores estáticos, ou seja, que não alteram durante o meu loop:

#nomes dos pães
nome_frances = "Francês"
nome_doce = "Pão doce"
nome_forma = "Pão de fôrma"

#valores dos pães
valor_frances = 0.50
valor_frances = 5.00
valor_forma = 5.99

#quantidades dos pães
quantidade_frances = 15
quantidade_doce = 20
quantidade_forma = 18

#nome do atendente
nome_atendente = "Maria"

# nome bairro
bairro_barroco = "barroco"
bairro_sao_jose = "sao jose"

#valores fretes
frete_barroco = 5.00
frete_sao_jose = 15.00

#código venda, esse código irá sendo utilizado dentro do loop
codigo_venda = 98568

while True:#código para não dar erro no código que ainda não foi finalizado
    print(f'--Bem-vindo a padaria Desespero, sou a atendente {nome_atendente}')
    escolha = input(f'Temos os pães: {nome_frances, nome_doce, nome_forma}.\nQual você deseja? ')
    if escolha == nome_frances:
        quantidade = int(input('Qual a quantidade? '))
        if quantidade <= quantidade_frances:
            quantidade_frances -= quantidade
            pedido_de_paes = quantidade
            valor_compra = quantidade * valor_frances
            print(f'Seu pedido ficou em: R${valor_compra}.')
        else:
            print(f'Infelizmente só temos {quantidade_frances} pães no momento.')
            break

    forma_retirada = input('Formas de retirada: \n1: Retirar na loja \n2: Entregar no endereço\nDigite o número referente a sua escolha: ')
    if forma_retirada == "2":
        bairro_entrega = input(f'Opções disponíveis:\n 1: {bairro_barroco},\n 2: {bairro_sao_jose}\nDigite o número do bairro: ').lower()
        if bairro_entrega == "1":
            valor_frete = frete_barroco
            print(f'O valor do frete é R${valor_frete}')
        elif bairro_entrega == "2":
            valor_frete = frete_sao_jose
            print(f'O valor do frete é R${valor_frete}')
        else:
            print('Fora da área de entrega.')
            break
    elif forma_retirada == "1":
        valor_frete = 0.00
    else:
        break

    dados_cliente = input('Informe seu nome: ')
    forma_pagamento = input('Formas de pagamento: \n1 - dinheiro\n2- cartão\nDigite o número da forma de pagamento: ')
    if forma_pagamento == "1":
        forma_pagamento = "Dinheiro"
    else:
        forma_pagamento = "Cartão"
    
    código_atual = codigo_venda + 1

    print(f"O valor total da sua compra foi de R${valor_compra + valor_frete}")
    break