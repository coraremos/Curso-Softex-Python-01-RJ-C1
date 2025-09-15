from banco_dados import dados
from dados_cliente import obter_dados_cliente
from dados_pagamento import solicitar_forma_pagamento
from gerar_codigo import gerar_codigo_venda
from calcular_frete import calcula_frete
from gerenciar_produto import cadastrar_produto, atualizar_produto
from processamento_pedido import processar_pedido



print(dados())


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

        opcao = input('Escolha uma opcao: ')

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
            print(f'Valor total: R$ {valor_total:.2f}')
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

iniciar_programa()