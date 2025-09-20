def operar_biblioteca(self):
    while True:
        print("Bem-vindos a Biblioteca da Corar!\nEscolha sua ação:")
        print("1) Incluir livros à biblioteca")
        print("2) Listar livros")
        print("3) Sair")
        escolha = input("Digite o número da ação: ")
        
        #adicionar na lista do acervo
        if escolha == "1":
            titulo = input("Digite o título do livro que deseja adicionar: ")
            autor = input("Digite o nome do autor: ")
            novo_livro = Livro(titulo, autor)
            self.adicionar_livro(novo_livro)

        elif escolha == "2":
            self.listar_livros(self)

        elif escolha == "3":
            print('Fechando sistema.')
            break
        else:
            print("Escolha inválida!")