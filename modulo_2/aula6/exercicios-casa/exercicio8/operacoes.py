def operar_carro(carro):
    while True:
        print("\nEscolha sua ação:")
        print("1) Checar combustível no carro")
        print("2) Completar combustível")
        print("3) Dirigir")
        print("4) Sair")
        escolha = input("Digite o número da ação: ")
        
        if escolha == "1":
            carro.combustivel()
        elif escolha == "2":
            carro.abastecer(int(input("Digite quantos litros deseja completar: ")))
        elif escolha == "3":
            carro.dirigir(int(input("Digite quantos km serão dirigidos: ")))
        elif escolha == "4":
            print('Fechando sistema.')
            break
        else:
            print("Escolha inválida!")