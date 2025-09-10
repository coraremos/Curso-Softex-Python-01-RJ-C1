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
#fazendo junto com o professor:

#banco de dados, com todos os valores estáticos, ou seja, que não alteram durante o meu loop:

def dados() -> dict:
    '''carregar e retornar os dados de produtos, frete, e funcionários'''   
    return {
        'atendente': 'Maria',
        'paes': {
            "frances": {'nome': 'Pão Francês', 'valor': 0.50, 'quantidade': 15},
            "doce": {'nome': 'Pão Doce', 'valor': 5.00, 'quantidade': 20},
            "forma": {'nome': 'Pão de Forma', 'valor': 5.99, 'quantidade': 18},
        },
        'bairros': {
            "barroco": {'nome':'Barroco', 'frete': 5.00},
            "sao jose": {'nome':'São José', 'frete': 15},

        },
        "codigo_venda_base": 95875,
    } 

def obter_dados_cliente() -> dict:
    '''solicitar e retornar os dados do cliente'''
    nome = input('Informe seu nome: ')
    return {"nome": nome}

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

def gerar_codigo_venda(codigo_base: int) -> int:
    '''gera e retorna o código de venda'''
    return codigo_base + 1

def calcula_frete(bairros_disponiveis: dict) -> tuple[str, float] | None:
    ''' o "|" significa "ou": ou devolverá tupla ou devolverá nada '''
    '''Calcula o valor do frete com base no bairro de entrega'''
    print('Bairros disponíveis para entrega')

    while True:

        for bairro in bairros_disponiveis.values():
            print(f"- {bairro['nome']}")

        bairro_entrega_nome = input('Qual o bairro de entrega?').lower()

        bairro_encontrado = None

        for chave, bairro in bairros_disponiveis.values():
            if bairro["nome"].lower() == bairro_entrega_nome:
                bairro_encontrado = chave
                break
        
        if not bairro_encontrado:
            print("Bairro fora da área de entrega.")
        
        else:
            frete = bairros_disponiveis[bairro_encontrado]["frete"]
            return bairro_entrega_nome, frete
def cadastrar_produto(estoque:dict) -> None:
    '''permite ao atendente cadastrar um novo produto'''
    nome_produto = input('Digite o nome do novo produto (identificador)').lower().strip()

    if nome_produto in estoque:
        print('Erro! Produto já cadastrado com este identificador.')
        return
    
    try:
        nome_completo = input('Digite o nome completo do produto: ').strip()
        valor = float(input('Digite o valor do novo produto: '))
        quantidade = int(input('Digite a quantidade inicial do produto: '))

        if nome_produto and nome_completo and valor > 0 and quantidade > 0:
            estoque[nome_produto] = {"nome": nome_completo, "valor": valor, "quantidade": quantidade}
            print(f'Produto {nome_completo} cadastrado com sucesso!')
        
        else:
            print('Erro! Dados inválidos.')

    except ValueError:
        print('Erro! Entrada de dados inválida')
    
def atualizar_produto(estoque: dict) -> None:
    '''permite ao atendente atualizar um produto existente'''
    nome_produto = input('Digite o nome do produto para atualizar (identificador): ').lower()
    if nome_produto not in estoque:
        print('produto não cadastrado')
        return

    print(f'Produto '{estoque[nome_produto]}' selecionado.')
    escolha = input("O que deseja atualizar?\n \
                    1 - Valor;\n \
                    2 - Quantidade")
    
    try: 
        if escolha == "1":
            novo_valor = float(input("Digite o novo valor do produto: "))

            if novo_valor > 0:
                estoque[nome_produto]["valor"] = novo_valor
                print("Valor atualizado para R$ {novo_valor:.2f}.")
            else:
                print("Valor inválido")

        elif escolha == "2":
            nova_quantidade = int(input('Digite a nova quantidade do produto:'))
            
            if nova_quantidade > 0:
                estoque[nome_produto]["quantidade"] = nova_quantidade
                print(f"Quantidade atual de {estoque[nome_produto]["quantidade"]} itens.")

            else:
                print("Quantidade inválida!")

        else: 
            print("Erro! Opção inválida.")

    except ValueError:
        print('Erro! Entrada de dados inválida. Digite apenas números.')



'''
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

    
    código_atual = codigo_venda + 1

    print(f"O valor total da sua compra foi de R${valor_compra + valor_frete}")
    break

'''