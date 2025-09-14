'''SINTAXE:

def > cria uma função
nome() > executa uma função
return > devolve um valor e encerra a função
* > empacota argumentos em uma tupla
** > empacota argumentos nomeados em um dicionário
lambda > cria uma função de uma linha

--- ao criar uma def com formato pré definido usar "valor:str/int/bool/float"
--- ou apontar o em que formato o resultado irá RETORNAR "-> int: / bool: / etc

--- quando criar um kwargs/dicionário/**, entregar o valor como (chave="valor")
ex.: borda="recheada" > e irá retornar " {'borda': 'recheada'} "

'''


#---CHAMAR A FUNÇÃO: (def)INIR uma função - nome()

#'de' define a função -> sempre com letras minúsculas
def diga_oi():
    print("Oi! Tudo bem?")

#chamar a função para que ela execute
diga_oi()


#---DANDO PARÂMETROS PARA A FUNÇÃO:

def saudar(nome):
    print(f"Olá, {nome}!")

saudar('Maria')
saudar('João')

#RETURN

def somar(a,b):
    return a + b
    #devolve o valor para quem chamou a função

#a variável total guarda o valor retornado
total = somar(5,3)
print(total*2)

#RETURN com MÚLTIPLOS VALORES

def calcular_area_perimetro(base, altura):
    area = base * altura
    perimetro = 2* (base+altura)
    return area, perimetro

#chamando a função e recebendo a tupla
resultados = calcular_area_perimetro(5,10)
print(f"Resultado como tupla: {resultados}")

#tipagem - definir o tipo que irá receber e qual irá sair (com -> int: ou ou float: ou bool:)
def saudar_com_idade(nome: str, idade:int):
    return f"Olá, {nome}. Você tem {idade} anos."
saudação = saudar_com_idade('Cora',26)
print(saudação)


'''
Argumentos Variáveis (*args)
E se você não souber quantos argumentos a função vai receber? O *args (de arguments) permite que a função aceite um número variável de argumentos.

O * empacota todos os argumentos extras em uma tupla.
'''

def somar_todos_os_numeros(*numeros):
#cria uma lista com *numeros, ou seja, vários números
    total = 0
    for num in numeros:
        total += num
    return total

print(somar_todos_os_numeros(1,2,3))

'''
Argumentos Nomeados Variáveis (**kwargs)
O **kwargs (de keyword arguments) é para quando você quer passar um número variável de argumentos com um nome (chave).

O ** empacota os argumentos extras em um dicionário.
'''

def exibir_perfil(**info):
#transforma "info" em valor de dicionário ainda sem informações
    for chave, valor in info.items():
    # a função .items retorna a lista do dicionário: 
    # d = {'a': 1, 'b': 2} / "d.items()" retorna: "items([('a', 1), ('b', 2)])"
        print(f"{chave}: {valor}")

exibir_perfil(nome="Maria", idade="30", cidade="Rio")

'''
Funções Lambda: A Receita Rápida
Para tarefas muito simples, de uma única linha, podemos usar uma função lambda. 
Elas são funções anônimas (sem nome). 
'''
# como usar: "lambda argumentos: expressão"

dobrar = lambda x: x*2
#criou: uma variável "dobrar" para sempre aplicar a ação lambda informada num print
#criou: um argumento "x" para ser substituido por um valor
print(dobrar(5))
#print(variável(argumento))

'''
Use uma função com def para a maioria das tarefas. 
Elas são claras, podem ter várias linhas e são fáceis de entender.

Use uma lambda para tarefas muito rápidas e de uma única linha. 
Quando você precisa de uma função simples como argumento para outra função.
'''

