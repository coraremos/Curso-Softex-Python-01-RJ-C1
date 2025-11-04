'''Contagem de Palavras com Exceção

Refaça o exercício de frequência de palavras (Contagem) no dicionário. 
Use try/except dentro do loop para verificar 
se a palavra já existe como chave no dicionário, 
incrementando ou inicializando a contagem.

for, str.split(), try/except (KeyError), dict, print
'''

def contar_palavras(texto: str) -> dict:
    """Retorna um dicionário com a frequência de cada palavra no texto."""
    palavras = texto.split()
    contagem = {}
    for p in palavras:
        chave = p.strip('.,!?;:()[]{}"\'').lower()
        try:
            contagem[chave] += 1
        except KeyError:
            contagem[chave] = 1
    return contagem

if __name__ == "__main__":
    exemplo = "Olá, mundo! Olá mundo. Teste, teste: exemplo."
    print(contar_palavras(exemplo))