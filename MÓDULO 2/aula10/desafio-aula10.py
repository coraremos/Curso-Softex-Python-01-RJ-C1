'''
em desenvolvimento
'''
print('Análise de Dados de Acessos!')

registros_acessos = []

while True:
     try:

        usuario = input('Digite o nome de usuário (ou "parar" para sair): ')
        
        if usuario.lower() == 'parar':
            print('Obrigada pelos dados.')
            break
        
        while True: 
            status = int(input('Selecione o status (1 - Sucesso / 2 - Falha): '))
            if status != 1 and status != 2:
                  print('escolha a opção correta!')
            else:
                 break
            
        duracao_minutos = int(input('Digite a duração da sessão em minutos: '))

        registro = []
        registro.append(usuario)
        registro.append(status)
        registro.append(duracao_minutos)
        tupla = tuple(registro)
        registros_acessos.append(tupla)

     except ValueError:
            print("Erro: entrada inválida!.")

usuarios_sucesso = set()
minutos_cjt = set()
minutos_soma = 0

for usuario, status, duracao_minutos in registros_acessos:
    #MINUTOS
    if status == 1:
        usuarios_sucesso.add(usuario)
        minutos_cjt.add(duracao_minutos)

minutos_soma = sum(minutos_cjt)

print(f'Registros de acessos:{registros_acessos}.')
print(f'Usuários com acesso bem-sucedidos: {usuarios_sucesso}.')
print(f'Tempo total das sessões bem-sucedidas: {minutos_soma} minutos.')