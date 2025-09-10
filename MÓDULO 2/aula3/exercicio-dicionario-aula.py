clientes = [
    {"nome": "Ana", "idade": 21, "cidade": "São Paulo"},
    {"nome": "Bruno", "idade": 30, "cidade": "Rio de Janeiro"},
    {"nome": "Carlos", "idade": 25, "cidade": "São Paulo"},
    {"nome": "Diana", "idade": 45, "cidade": "Belo Horizonte"},
    {"nome": "Eduarda", "idade": 30, "cidade": "Rio de Janeiro"},
    {"nome": "Fábio", "idade": 25, "cidade": "São Paulo"},
]


print("--- Lista de Clientes ---")
for cliente in clientes:
    nome = cliente["nome"]
    idade = cliente["idade"]
    print(f"Nome: {nome}, Idade: {idade}")

soma_idades = 0
total_clientes = 0

for cliente in clientes:
    soma_idades += cliente["idade"]

total_clientes = len(clientes)
idade_media = soma_idades / total_clientes
print(f"\nIdade média dos clientes: {idade_media:.2f} anos")

clientes_por_cidade = {}

for cliente in clientes:
    cidade = cliente["cidade"]
    if cidade in clientes_por_cidade:
        clientes_por_cidade[cidade] += 1
    else:
        clientes_por_cidade[cidade] = 1

print("\n--- Clientes por Cidade ---")
print(clientes_por_cidade)


''' ENUNCIADO

Exercício: Análise de Dados de Clientes

Imagine que você trabalha em uma loja e precisa analisar dados de clientes para entender
melhor o seu público. Você tem uma lista de dicionários, onde cada dicionário representa um
cliente.

O Desafio

1. Crie a lista de dicionários clientes fornecida abaixo.
2. Percorra a lista e, para cada cliente, imprima o nome e a idade.
3. Calcule e imprima a idade média de todos os clientes.
4. Crie um novo dicionário que conte a quantidade de clientes por cidade. A chave deve ser
a cidade e o valor deve ser o total de clientes dessa cidade.

Dados de Clientes

clientes = [
{"nome": "Ana", "idade": 25, "cidade": "São Paulo"},
{"nome": "Bruno", "idade": 30, "cidade": "Rio de Janeiro"},
{"nome": "Carlos", "idade": 25, "cidade": "São Paulo"},
{"nome": "Diana", "idade": 45, "cidade": "Belo Horizonte"},
{"nome": "Eduarda", "idade": 30, "cidade": "Rio de Janeiro"},
{"nome": "Fábio", "idade": 25, "cidade": "São Paulo"}
]
'''