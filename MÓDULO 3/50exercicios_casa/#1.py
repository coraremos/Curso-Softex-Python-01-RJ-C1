'''
Crie uma função que receba duas listas de números inteiros geradas com random. 
Retorne uma nova lista contendo apenas os elementos que estão presentes em ambas as listas, sem repetição.

Ferramentas sugeridas: função, random, set (para eficiência), print'''

''' #PRIMEIRO RACIOCÍNIO
def lista_de_numeros_aleatorios():
    import random
    lista = list(range(1, 11))
    lista_um = random.sample(lista, k=5) #gera uma lista onde os números não se repetem]
    lista_dois = random.sample(lista, k=5) #gera uma lista onde os números não se repetem]
    lista_completa = set(lista_um+lista_dois)
    lista_completa = list(lista_completa)
    print(f"Primeira lista: {lista_um}")
    print(f"Segunda lista: {lista_dois}")
    return lista_completa
    
print(lista_de_numeros_aleatorios())'''

#FORMA FINAL RESUMIDA

def lista_de_numeros_aleatorios():

    import random 

    #criar lista 1 e lista 2, de 5 números aleatórios, dentro dos números de 1 a 10
    L1 = random.sample( range(1, 11) , 5)
    L2 = random.sample( range(1, 11) , 5)

    #somente para visualizar as listas
    print(f"Primeira lista: { list(L1) }")
    print(f"Segunda lista: { list(L2) }\n")

    lista = set( L1+L2 ) #transforma a soma das duas listas em um conjunto e ordena as informações
    print(f'A lista somada e transformada em conjunto fica assim: {lista}\n')
    return f'Essa é a lista aleatória: { list( lista ) }'
    
print(lista_de_numeros_aleatorios())