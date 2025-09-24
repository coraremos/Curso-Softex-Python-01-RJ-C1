#2. Nível Médio: Sistema de Mídia

#Crie uma classe base Midia com um construtor que recebe titulo e duracao_seg. 
class Midia:
    def __init__(self, titulo, duracao_seg):
        self._titulo = titulo
        self._duracao_seg = duracao_seg

    # Adicione um método exibir() que imprime o título e a duração.
    def exibir(self):
        print(f"O título é: {self._titulo}, e a duração: {self._duracao}.)

#Crie duas classes filhas, Musica e Video, que herdam de Midia:
class Musica(Midia):

    #● Musica deve ter um atributo adicional artista 
    def __init__(self, titulo, duracao_seg, artista):
        super().__init__(titulo, duracao_seg)
        self._artista = artista

    # e sobrescrever o método exibir() para incluir o nome do artista.
    def exibir(self):
        print(f"O nome do artista é: {self._artista}.)

class Video(Midia):
    #● Video deve ter um atributo adicional resolucao 
    
    def __init__(self, titulo, duracao_seg, resolucao):
        super().__init__(titulo, duracao_seg)
        self._resolucao = resolucao
    
    # e sobrescrever o método exibir() para incluir a resolução.
    def exibir(self):
        print(f"O vídeo é: {self._resolucao}.)

#No script principal, crie um dicionário 
# para organizar sua coleção de mídias, usando as chaves 'musicas' e 'videos'.

#Crie objetos de Musica e Video e os adicione a suas respectivas listas dentro do dicionário. 
#Por fim, itere sobre as listas e chame o método exibir() para cada item, demonstrando o polimorfismo de forma organizada.