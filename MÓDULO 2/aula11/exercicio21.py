'''
21. Agenda de Contatos: Crie um sistema simples de agenda que use um dicionário. Use
um loop while para mostrar um menu com opções de "adicionar contato", "buscar
contato" e "sair".
'''

agenda_contatos = {}

while True:

    print('---Agenda de contatos---')
    print('1. Adicionar contato')
    print('2. Buscar contato')
    print('3. Ver lista de contatos')
    print('4. Sair')

    try:
        escolha = input('Digite a opção desejada: ')
        escolha = int(escolha)
    except ValueError:
        print('Opção inválida, digite uma das opções oferecidas:')
        continue

    if escolha == 1:
        agenda_contatos["contato"] = input('Qual contato deseja adicionar?').lower()

#estudar e corrigir essa parte
    elif escolha == 2:
        nome = input('Digite o contato que deseja encontrar: ')
        if nome in agenda_contatos.value():
            print(f'Contato {nome} já existe na agenda!')
        else:
            print(f'Contato {nome} não existe')

    elif escolha == 3:
        print(agenda_contatos')
              
    elif escolha == 4:
        print('Finalizando a consulta.')
    else:
        print('Opção inválida, digite uma das opções oferecidas:')