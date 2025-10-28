"""Transposição de Matriz (LISTAS DENTRO DE LISTAS)

Dada uma lista de listas (matriz $N \times M$), 
crie uma função para transpor a matriz (linhas viram colunas). 
Use list comprehension aninhada.

função, list comprehension (aninhada), range(), print


"""

def transpor_matriz(matriz: list[list]) -> list[list]:

    # validar que a matriz não é vazia e que é retangular para evitar IndexError.
    if not matriz:
        return []
    col_count = len(matriz[0])
    if any(len(linha) != col_count for linha in matriz):
        raise ValueError("A matriz deve ser retangular (todas as linhas com mesmo comprimento).")
    
    #list comprehension
    return [[linha[i] for linha in matriz] for i in range(col_count)]

# retangular
m = [[1,2,3],[4,5,6]]
print(transpor_matriz(m))
# == [[1,4],[2,5],[3,6]]

# quadrado
m = [[1,2],[3,4]]
print(transpor_matriz(m)) 
# == [[1,3],[2,4]]

# vazio
print(transpor_matriz([])) 
# == []

# com pytest.raises(ValueError):
print(transpor_matriz([[1,2],[3]]))

