
def operar_biblioteca(self):
    while True:
        print("Bem-vindos a Biblioteca da Corar!\nEscolha sua ação:")
        print("1) Incluir livros à biblioteca")
        print("2) Listar livros")
        print("3) Sair")
        escolha = input("Digite o número da ação: ")
        
        if escolha == "1":
            self.livro = input("Digite o título do livro que deseja adicionar: ")
            self.autor = input("Digite o nome do autor: ")
            adicionar_livro()
            
        elif escolha == "2":
            self.listar_livros()
        elif escolha == "3":
            print('Fechando sistema.')
            break
        else:
            print("Escolha inválida!")


#Crie uma biblioteca, crie alguns objetos Livro e adicione-os à biblioteca. Depois, liste os livros.