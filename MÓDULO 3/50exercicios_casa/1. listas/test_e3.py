from e3 import editar_lista
import pytest

def test_editar_lista():
    lista = ['a', 'b', 'A', 'c']
    saida = ['b', 'c']
    assert editar_lista(lista) == saida

