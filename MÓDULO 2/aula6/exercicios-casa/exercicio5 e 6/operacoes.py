def operar_conta(conta):
    while True:
        print("\nEscolha sua ação:")
        print("1) Ver saldo")
        print("2) Depositar")
        print("3) Sacar")
        print("4) Sair")
        escolha = input("Digite o número da ação: ")
        
        if escolha == "1":
            conta.extrato()
        elif escolha == "2":
            conta.depositar(float(input("Digite o valor que deseja depositar: ")))
        elif escolha == "3":
            conta.sacar(float(input("Digite o valor que deseja sacar: ")))
        elif escolha == "4":
            print('Fechando sistema.')
        else:
            print("Escolha inválida!")
    