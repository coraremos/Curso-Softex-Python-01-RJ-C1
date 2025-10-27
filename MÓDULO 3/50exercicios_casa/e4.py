'''
Dada uma lista, use list comprehension para criar uma nova lista que retém apenas os números, descartando strings, booleanos ou outro

list comprehension, isinstance(), if, print
'''

lista = ['a', 'b', 3, 2]
lista_numeros = [item for item in lista if isinstance(item, int)]

print(lista_numeros)

