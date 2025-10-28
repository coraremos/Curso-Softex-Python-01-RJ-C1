from e6 import transpor_matriz
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