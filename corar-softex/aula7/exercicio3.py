'''
EXERCICIO 3: menu de comandos para um robô
Crie um programa que simula o controle de um robô simples com um menu de comandos.
1. O robô pode estar em uma posição inicial (você pode usar uma variável para isso, por exemplo, a posição 0)
2. O programa deve exibir um menu com as seguintes opções: 1 - Avançar, 2 - Recuar, 3 - Status, 4 - Desligar.
3. Peça ao usuário para escolher um comando.
4. Com base na escolha execute a ação correspondente:
    - Avançar: Adicione um valor à posição do robô.
    - Recuar: Subtraia um valor da posição do robô.
    - Status: Mostre a posição atual do robô.
    - Desligar: Encerre o programa.
5. O menu deve continuar aparecendo apís cada comando, até que o usuário escolha a opção "Desligar".
6. Se o usuário digitar um comando inválido, exiba uma mensagem de erro.
'''

posicao = 0
titulo = print('Olá, eu sou um robô!')
while True:
    comando = input('Escolha um comando para que eu possa andar:\n1- Avançar\n2- Recuar\n3- Status\n4- Desligar\nInsira o número da ação: '))
    if comando == '1':
        posicao += 1
    elif comando == '2':
        posicao -= 1
    elif comando == '3':
        print(f'\nMINHA POSIÇÃO ATUAL É {posicao}.\n')
    elif comando == '4':
        print('Programa encerrado.')
        break
    else:
        print('\nComando inválido.\n')
        
    