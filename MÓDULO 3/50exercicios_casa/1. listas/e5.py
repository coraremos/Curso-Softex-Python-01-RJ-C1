'''Encontrar Duplicatas

Crie uma função que receba uma lista. OK
Retorne uma lista de tuplas, onde:
cada tupla 
contém o elemento duplicado 
e sua frequência 
na lista original.

função, for, dict (para contagem), list, print
'''
from collections import Counter

def verificar_duplicatas(lista:list) -> list[tuple]:
    """Retorna uma lista de tuplas (elemento, frequência) apenas para elementos duplicados."""
    counts = Counter(lista)
    
    return [
        (item, freq) 
        for item, freq 
        in counts.items() 
        if freq > 1
        ]
    """ new_list = [expressão for item in interável if condição]
        base: Retorna uma lista "[]";
        expressão: que gera os valores 'item' e 'frequência' em tupla;
        for: para cada item,frequência dentro da contagem dos itens
        condição: somente considerar se a frequência for maior que um"""

lista = ['a', 'b', 'c', 'd', 'a', 'f', 'b', 'c', 'a']
print(verificar_duplicatas(lista))