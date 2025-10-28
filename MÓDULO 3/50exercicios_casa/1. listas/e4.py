'''Compressão de Lista

Dada uma lista, use list comprehension para criar 
uma nova lista que retém apenas os números, 
descartando strings, booleanos ou outro

Usar list comprehension, isinstance(), if, print
'''

def cria_lista_numeros(lista:list):
    lista_numeros = [item for item in lista if type(item) is int]

    return lista_numeros

lista_mesclada = ['a', False, 'b', 3, 2]
print(cria_lista_numeros(lista_mesclada))

