''' import random


opcoes = ["pedra", "papel", "tesoura"]
while True:
    escolha_computador = random.choice(opcoes)

    escolha_usuario = input('Escolha Pedra, Papel ou Tesoura: ').lower()
    if escolha_usuario not in opcoes:
        print('Opção inválida. Tente novamente.')
        continue
    print(f'O computador escolheu: {escolha_computador.upper()}')

    if escolha_usuario == escolha_computador:
        print('Empate!')
    elif escolha_usuario == "pedra" and escolha_computador == "tesoura":
        print('Você Venceu!')
    elif escolha_usuario == "papel" and escolha_computador == "pedra":
        print('Você Venceu!')    
    elif escolha_usuario == "tesoura" and escolha_computador == "papel":
        print('Você Venceu!')
    else:
        print('PerdeL mané!')

    # Pergunta se o usuário quer jogar novamente 
    jogar_novamente = input("Jogar novamente? (s/n): ").lower() 
    if jogar_novamente != "s": 
        break # O 'break' sai do loop, encerrando o jogo print("Obrigado por jogar!")
    else:
        print('OBA!!!')
print('Gratidão por jogar!')
'''