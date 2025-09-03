''' Exercício 4: Análise de Notas

Você tem uma lista de tuplas (aluno, nota).
1. Identifique e imprima a maior nota alcançada.
2. Crie uma tupla com todos os alunos que tiraram a maior nota.
3. Crie um conjunto de todos os alunos que tiveram uma nota menor que 7.0.

O que vai entrar:

notas = [("Ana", 9.5), ("João", 8.0), ("Maria", 10.0), ("Pedro", 7.5), ("Ana", 10.0), ("Carlos", 6.5)]

A saída esperada:

A maior nota alcançada é: 10.0

Alunos que tiraram a maior nota: ('Maria', 'Ana')

Alunos que tiveram nota menor que 7.0: {'Carlos'}
'''

notas = [
    ("Ana", 9.5), 
    ("João", 8.0), 
    ("Maria", 10.0), 
    ("Pedro", 7.5), 
    ("Ana", 10.0), 
    ("Carlos", 6.5)
]

#transformar em conjunto
somente_nota = set()
maior_nota = []



for aluno, nota in notas:
    #ordenar em forma crescente
    add()
    notas_ordem_crescente = sorted(somente_nota)
    if nota notas_ordem_crescente[-1]:
        notas.add(maior_nota)
    print(f'A maior nota alcançada é: {maior nota}')


'''resolução professor:

notas = [
    ("Ana", 9.5),
    ("João", 8.0),
    ("Maria", 10.0),
    ("Pedro", 7.5),
    ("Ana", 10.0),
    ("Carlos", 6.5),
]


maior_nota = 0.0
for _, nota in notas:
    if nota > maior_nota:
        maior_nota = nota
print(f"A maior nota alcançada é: {maior_nota}")

alunos_maior_nota = []
for aluno, nota in notas:
    if nota == maior_nota:
        alunos_maior_nota.append(aluno)
alunos_maior_nota = tuple(alunos_maior_nota)
print(f"\nAlunos que tiraram a maior nota: {alunos_maior_nota}")

alunos_nota_baixa = {aluno for aluno, nota in notas if nota < 7.0}
print(f"\nAlunos que tiveram nota menor que 7.0: {alunos_nota_baixa}")
'''