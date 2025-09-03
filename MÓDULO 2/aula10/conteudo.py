'''
ESTRUTURAS DE DADOS:

_______________________________________________________
TUPLAS - tuple: coleções ordenadas e imutáveis

    separadas por () 
    finaliza sempre com uma vírgula
    DÁ PRA ACESSAR OS ITENS COM INDEX igual listas
    OS ITENS NÃO PODEM SER ALTERADOS
    usada normalmente para ponto cardinal, coordenada geográficas ou cores

.count()
.index()

tuple() 
#converte uma lista em uma tupla

list() 
#converte uma tupla em lista
______________________________________________________
LISTA COM TUPLAS: 
(pra mais de uma variavel temporária(no 'for'), se não tiver todas as duas informações dentro de todas as tuplas ou mais que as variaveis, dá erro!)

pessoas = [("Ana", 25),("Bruno", 30),("Carlos",28),]
for nome, idade in pessoas:
    print(f'{} tem {} anos.')
_______________________________________________________
CONJUNTOS - set: coleções desordenadas e mutáveis de itens únicos

separados por {}
não tem duplicatas: automaticamente remove valores repetidos

conjunto_vazio = set() 
#usar {} cria um dicionário vazio

set() #set transforma lista em conjunto, para filtrar itens repetidos!!!

add() ou 
.remove() #se nao existir item dá erro
.discard() #remove mesmo sem existir item, sem dar erro (1 valor de cada vez)
.union()
.intersection()
.difference()
.symmetric_difference()
________________________________________________________
UM CONJUNTO DE TUPLAS:

produtos = {
    ("produto1", 10, 2.5),
    ("produto2", 5, 4.0),
    ("produto3", 8, 3.25)
}

for nome, qtd, preço in produtos:
total = qtd * preco
print (f"{nome}: {qtd} unidades x R${preco:.2f} = R${total:.2f}")

'''

numeros = {1,2,3}
numeros.add(4)
print(f'conjunto após 'add(4)': {numeros}')
      
'''

'''      

A = {}
B = {}

UNIAO = A.union(B)
print(f'União:{uniao}')
#saída {1,2,3,4,5,6}

A.intersection()
B.difference()

'''
quando os dados não devem ser alterados

'''

minha_tupla = (1,2,3,4,2)
minha_tupla.count(2) #resulta 2
minha_tupla.index(2) #resulta 3

_______________________________________________________
ANOTACOES

vendas = [
    ("Teclado", 50, 2), 
    ("Mouse", 25.50, 4), 
    ("Monitor", 300, 1), 
    ("Fone", 45, 1),
    ("Webcam", 75.20, 2)
]

vendas_tupla= []
for nome_do_produto, valor, quantidade in vendas:
    vendas_tupla.append((nome_do_produto, valor, quantidade))
print(vendas_tupla) #transforma formato LISTA em formato TUPLA

vendas_conjunto = [] #transforma formato LISTA em formato CONJUNTO
for nome_do_produto, valor, quantidade in vendas:
    vendas_conjunto.append({nome_do_produto, valor, quantidade})
print(vendas_conjunto)

#TUPLA É IMUTAVEL
#CONJUNTO FILTRA AS DUPLICIDADES
#LISTA É ALTERÁVEL
