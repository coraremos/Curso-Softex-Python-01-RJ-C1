'''Remoção Condicional com While

Use um loop while para iterar sobre uma lista de strings. 
Remova todas as strings que contêm a letra 'a' (minúscula ou maiúscula). 
Atenção: Mudar o tamanho da lista durante a iteração requer cuidado 
(ex: iterar de trás para frente ou usar um índice while).

Ferramentas sugeridas: while, list.pop()/list.remove(), str.lower(), if, print'''

def editar_lista(lista:list):
    n = len(lista) - 1
    while n >=0:    
        if 'a' in lista[n].lower():
            lista.pop(n)
        n-=1
    return lista

lista = ['a', 'b', 'A', 'c']
print(editar_lista(lista))

