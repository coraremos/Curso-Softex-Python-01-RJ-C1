from e3 import editar_lista

def test_editar_lista():
    lista = ['a', 'b', 'A', 'c']
    saida = ['b', 'c']
    assert editar_lista(lista) == saida