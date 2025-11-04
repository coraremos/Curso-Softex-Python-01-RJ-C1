from e6 import transpor_matriz
from e6 import linhas_para_colunas
import pytest

def test_transpor_retangular():
    m = [[1,2,3],[4,5,6]]
    assert transpor_matriz(m) == [[1,4],[2,5],[3,6]]

def test_transpor_quadrado():
    m = [[1,2],[3,4]]
    assert transpor_matriz(m) == [[1,3],[2,4]]

def test_transpor_vazio():
    assert transpor_matriz([]) == []

def test_transpor_non_rectangular_raises():
    with pytest.raises(ValueError):
        transpor_matriz([[1,2],[3]])

#MENTORIA

def test_coversao_matriz():
    entrada = [[1, 2, 3], [4, 5, 6]]
    saida = [[1, 4], [2, 5], [3, 6]]

    entrada_2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    saida_2 = [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

    assert linhas_para_colunas(entrada) == saida
    assert linhas_para_colunas(entrada_2) == saida_2

