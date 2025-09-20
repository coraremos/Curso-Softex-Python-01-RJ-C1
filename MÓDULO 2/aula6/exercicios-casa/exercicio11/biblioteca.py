#Exercício 11: Biblioteca de Livros

#Crie duas classes: Livro e Biblioteca.

#1. A classe Livro terá atributos título e autor.
class Livro:
    def __init__(self, titulo:str, autor:str) -> None:
        self.titulo = titulo
        self.autor = autor

#2. A classe Biblioteca terá um atributo acervo, que começa como uma lista vazia [].
class Biblioteca:
    def __init__(self):
        self.acervo = [] 

    #adicionar_livro(livro)
    def adicionar_livro(self, livro: Livro):
        '''recebe um objeto Livro e o adiciona à lista acervo.'''
        self.acervo.append(livro)    

    def listar_livros(self):
        '''percorre a lista acervo e imprime o título e o autor de cada livro.'''
        for livro in self.acervo:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}")


