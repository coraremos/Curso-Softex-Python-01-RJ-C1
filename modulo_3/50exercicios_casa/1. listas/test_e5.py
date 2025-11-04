from e5 import verificar_duplicatas
import pytest

def test_verificar_duplicadas():
    lista = ['a', 'b', 'c', 'd', 'a', 'f', 'b', 'c', 'a']
    saida = [('a', 3), ('b', 2), ('c', 2)]
    assert verificar_duplicatas(lista) == saida