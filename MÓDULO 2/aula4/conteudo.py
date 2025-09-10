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
saudar_com_idade('cora',26)


