'''
Crie uma função que receba uma lista e um inteiro k. 
A função deve rotacionar a lista k posições para a direita. 
Use slicing de lista para resolver.

função, list slicing, print
'''

def rotacionar_lista(lista:list, k:int) -> list:
    return lista[-k:] + lista[:-k]

lista_de_espera = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto', 'sétimo', 'oitavo', 'nono', 'décimo']
print(rotacionar_lista(lista_de_espera,1))