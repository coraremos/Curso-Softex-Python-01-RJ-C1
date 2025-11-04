from pytest_treino.src.operations.add import AddOperation
import pytest

addOperation = AddOperation()


@pytest.mark.parametrize('num1, num2, result',
        [
            (3, 2, 5),
            (4, 1, 5)
        ]
)

def test_soma(num1, num2, result):
    assert addOperation.soma(num1,num2) == result