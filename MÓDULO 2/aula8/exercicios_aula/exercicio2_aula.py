#2. Nível Médio: Sistema de Mídia

#Crie uma classe base Midia com um construtor que recebe titulo e duracao_seg. 
class Midia:
    def __init__(self, titulo:str, duracao_seg:int):
        self.titulo = titulo
        self.duracao_seg = duracao_seg

    # Adicione um método exibir() que imprime o título e a duração.
    def exibir(self):
        print(f"Título: {self.titulo}, Duração: {self.duracao_seg}.")

    def __str__(self):
        return(f"{self.titulo}")

#Crie duas classes filhas, Musica e Video, que herdam de Midia:
class Musica(Midia):

    #● Musica deve ter um atributo adicional artista 
    def __init__(self, titulo, duracao_seg, artista:str):
        super().__init__(titulo, duracao_seg)
        self.artista = artista

    # e sobrescrever o método exibir() para incluir o nome do artista.
    def exibir(self):
        print(f"Título: {self.titulo}, Duração: {self.duracao_seg}, Artista: {self.artista}.")

class Video(Midia):
    #● Video deve ter um atributo adicional resolucao 
    
    def __init__(self, titulo, duracao_seg, resolucao:str):
        super().__init__(titulo, duracao_seg)
        self.resolucao = resolucao
    
    # e sobrescrever o método exibir() para incluir a resolução.
    def exibir(self):
        print(f"Título: {self.titulo}, Duração: {self.duracao_seg}, Resolução: {self.resolucao}.")

m1 = Musica("Lalala", 30, "Zé")
v1 = Video("Toc-toc", 60, "1600x1200")

#No script principal, crie um dicionário 
# para organizar sua coleção de mídias, usando as chaves 'musicas' e 'videos'.

dicionarios_midia = {"musicas":[], "videos":[]}
dicionarios_midia["musicas"].append(m1)
dicionarios_midia["videos"].append(v1)

#Crie objetos de Musica e Video e os adicione a suas respectivas listas dentro do dicionário. 
#Por fim, itere sobre as listas e chame o método exibir() para cada item, demonstrando o polimorfismo de forma organizada.

print(dicionarios_midia)

for item in dicionarios_midia.values():
    for midia in item:
        midia.exibir()

