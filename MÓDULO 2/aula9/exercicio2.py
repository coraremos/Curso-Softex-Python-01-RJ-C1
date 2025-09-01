lista1 = ["vermelho", "azul", "verde", "amarelo"]
lista2 = ["verde", "roxo", "azul", "preto"]
lista = []
for i in lista1:
    for y in lista2:
        if i == y:
            lista.append(i)
print(lista)

'''
ENUNCIADO

Nível 2: Combinando Lógica
Aqui, você vai usar mais de uma lista e combinar diferentes lógicas de controle, como loops e
verificações de pertencimento.
Exercício 2: Encontrando Elementos Comuns
Você tem duas listas e precisa encontrar os elementos que aparecem em ambas. O programa
deve gerar uma terceira lista contendo apenas os elementos em comum, sem repetições.
● Entrada: Duas listas.
● Saída: Uma nova lista com os elementos que as duas listas têm em comum.
Exemplo:
lista1 = ["vermelho", "azul", "verde", "amarelo"]
lista2 = ["verde", "roxo", "azul", "preto"]
Resultado Esperado:
['azul', 'verde']
'''

'''
resolução do prof. 

lista1 = ["vermelho", "azul", "verde", "amarelo"]
lista2 = ["verde", "roxo", "azul", "preto"]
elementos_comuns = []

for item in lista1:
    if item in lista2 and item not in elementos_comuns:
        elementos_comuns.append(item)
        
print(f'lista 1: {lista1}')
print(f'lista 2: {lista2}')
print(f"elementos em comum: {elementos_comuns}")
'''