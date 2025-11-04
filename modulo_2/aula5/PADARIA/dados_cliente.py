def obter_dados_cliente() -> dict:
    '''solicitar e retornar os dados do cliente'''
    nome = input('Informe seu nome: ')
    return {"nome": nome}