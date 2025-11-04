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

def cadastrar_localidade(bairros: dict) -> None:
    '''Permite ao atendente cadastrar um novo bairro para entrega'''
    nome_bairro = input('Digite o nome do bairro (identificador)').lower().strip()
    if nome_bairro in bairros:
        print('Erro! Bairro já cadastrado.')
        return
    
    try:
        nome_completo = input('Digite o nome completo do bairro: ').lower().strip()
        valor_frete = float(input(f'Digite o valor do frete para o bairro{nome_completo}:'))

        if nome_bairro and valor_frete >= 0 and nome_completo:
            bairros['nome_bairro'] = {'nome': nome_completo, 'frete': valor_frete}
            print(f"Localidade {nome_completo} com frete de R$ {valor_frete:.2f} cadastrado com sucesso!")
        else:
            print("Dados inválidos! O cadastro não foi realizado.")
            return

    except ValueError:
        print('Entrada inválida! O valor do frete deve ser um número.')

def processar_pedido(paes_disponiveis: dict) -> tuple[dict, int, float, dict] | None:
    '''Processa o pedido do cliente, verifica o estoque  e calcula o frete. 
    Retorna uma tupla com o dicionário do pão, quantidade, 
    valor total da compra e o dicionário atualizado de pães'''
    
    print('Temos os seguintes pães: ')
    for pao in paes_disponiveis.values():
        print(f' - {pao["nome"]}')

    escolha_pao = input('Qual pão você deseja? ').lower().strip()
    pao_encontrado = None

    for chave, pao in paes_disponiveis.items():
        if pao['nome'].lower() == escolha_pao:
            pao_encontrado = chave
            break

    if not pao_encontrado:
        print('Opção inválida!')
        return None
    
    pao_escolhido = paes_disponiveis[pao_encontrado]

    try:

        quantidade = int(input(f'Digite a quantidade do {pao_escolhido["nome"]}:'))
        if quantidade <= 0:
            print('Quantidade inválida!')
            return None
        
    except ValueError:
        print('Erro! Quantidade deve ser um número inteiro.')
        return None

    if quantidade > pao_escolhido['quantidade']:
        print(f'Infelizmente só temos {pao_escolhido["quantidade"]} unidades deste pão.')
        return None

    paes_disponiveis[pao_encontrado]['quantidade'] -= quantidade
    valor_compra = quantidade * pao_escolhido['valor']
    return pao_escolhido, quantidade, valor_compra, paes_disponiveis

def iniciar_programa() -> None:
    banco_dados = dados()
    atendente = banco_dados['atendente']
    paes_estoque = banco_dados['paes']
    bairros_disponiveis = banco_dados['bairros']
    codigo_venda = banco_dados['codigo_venda_base']

    while True:
        print(f'\nBem-vindo(a) à Padaria Desespero, sou o(a) atendente {atendente}.\n')
        print('--- Menu principal ---')
        print('1- Iniciar vendas')
        print('2- Gerenciar produtos')
        print('3- Cadastrar nova localidade')
        print('4- Sair do sistema')

        opcao = input('Escolha uma opção: ')

        if opcao == "1":
            pedido = processar_pedido(paes_estoque)
            if not pedido:
                continue

#colocando as informações de cada valor na variável, em forma de tupla:
            pao_escolhido, quantidade, valor_compra, paes_estoque = pedido
            print(f'Você escolheu {quantidade} unidade(s) de {pao_escolhido["nome"]}, totalizando R$ {valor_compra:.2f}.')  

            forma_retirada = input('Você deseja retirar na loja ou entregar? (1-Retirar, 2-Entregar): ')
            valor_frete = 0.0
            if forma_retirada == "2":
                bairro, valor_frete = calcula_frete(bairros_disponiveis)
                print(f'O valor do frete para {bairros_disponiveis[bairro]["nome"]} é R$ {valor_frete:.2f}.')

            dados_cliente = obter_dados_cliente()
            forma_pagamento = solicitar_forma_pagamento()

            valor_total = valor_compra + valor_frete
            cod_venda = gerar_codigo_venda(codigo_venda)
            banco_dados['codigo_venda_base'] = cod_venda

            print('\n--- Resumo do pedido ---')
            print(f'Cliente: {dados_cliente["nome"]}')
            print(f'Produto: {pao_escolhido["nome"]} - Quantidade: {quantidade} - Valor: R$ {valor_compra:.2f}')
            print(f'Valor do frete: R$ {valor_frete:.2f}')
            print(f'Forma de pagamento: {forma_pagamento}')
            print(f'Valor total: R$ {valor_total_compra}')
            print(f'Código da entrega: {cod_venda}')
                
        elif opcao == "2":
            pass
        elif opcao == "3":
            pass
        elif opcao == "4":
            print('Encerrando o sistema. Até logo!')
            break
        else:
            print('Opção inválida! Tente novamente.')