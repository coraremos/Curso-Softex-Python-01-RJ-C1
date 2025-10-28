from e7 import kadane  # ou do arquivo onde sua função está

def test_kadane_misto():
    assert kadane([-2,1,-3,4,-1,2,1,-5,4]) == (6, 3, 6)

def test_kadane_todos_positivos():
    assert kadane([1,2,3,4]) == (10, 0, 3)

def test_kadane_todos_negativos():
    assert kadane([-5,-2,-3])[0] == -2  # aceita índice qualquer, validamos soma

def test_kadane_vazia():
    assert kadane([]) is None