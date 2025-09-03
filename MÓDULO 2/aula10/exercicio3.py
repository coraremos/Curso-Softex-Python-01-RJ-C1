'''
Exercício 3: Sistema de Login

Você tem uma lista de tuplas, onde cada tupla é um registro de acesso (usuario, status_login).

O status_login pode ser 'sucesso' ou 'falha'.

Usando laços de repetição e condicionais, identifique e imprima:
1. O nome dos usuários que tiveram pelo menos um login bem-sucedido.
2. O nome dos usuários que tiveram somente logins com falha.

O que vai entrar:
acessos = [("Pedro", "sucesso"), ("Ana", "falha"), ("Maria", "sucesso"), ("Pedro", "falha"),
("Ana", "falha")]
A saída esperada:
Usuários com pelo menos um login bem-sucedido:
{'Maria', 'Pedro'}
Usuários que tiveram somente logins com falha:
{'Ana'}
'''

acessos = [
    ("Pedro", "sucesso"), 
    ("Ana", "falha"), 
    ("Maria", "sucesso"), 
    ("Pedro", "falha"),
    ("Ana", "falha")
]

#CRIAR CONJUNTOS VAZIOS
login_ok = set()
login_falha = set()

#PARA ADICIONAR EM CONJUNTO USAR '.ADD'
for usuario, status_login in acessos:

# O nome dos usuários que tiveram pelo menos um login bem-sucedido.
    if status_login == 'sucesso':
        login_ok.add(usuario)
        
# O nome dos usuários que tiveram somente logins com falha.
    elif status_login == 'falha':
        login_falha.add(usuario)
        
#diferença do usuario que está no conjunto de falha mas não está no conjunto de sucesso
    falha = login_falha.difference(login_ok)

print(f'usuarios com sucesso: {login_ok}')
print(f'\nusuarios com falha: {login_falha}')
print(f'\nUsuários com pelo menos um login bem-sucedido: {login_ok}')
print(f'\nUsuários que tiveram somente logins com falha: {falha}\n.')