'''Use um loop while para iterar sobre uma lista de strings. 
Remova todas as strings que contêm a letra 'a' (minúscula ou maiúscula). 
Atenção: Mudar o tamanho da lista durante a iteração requer cuidado 
(ex: iterar de trás para frente ou usar um índice while).

Ferramentas sugeridas: while, list.pop()/list.remove(), str.lower(), if, print'''

def editar_lista(lista:list):

    for n in lista:
        
        if 'a' in n:
            lista.remove(n)
    return lista

lista = ['a', 'b', 'A', 'c']
print(editar_lista(lista))

