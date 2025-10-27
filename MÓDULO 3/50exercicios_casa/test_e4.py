from e4 import cria_lista_numeros

def test_cria_lista_numeros():
    lista_mesclada = ['a', False, 'b', 3, 2]
    saida = [3, 2]
    assert cria_lista_numeros(lista_mesclada) == saida