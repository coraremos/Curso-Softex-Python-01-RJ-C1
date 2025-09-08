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
            
        duracao_minutos = float(input('Digite a duração da sessão em minutos: '))

        registro = []
        registro.append(usuario)
        registro.append(status)
        registro.append(duracao_minutos)
        tuple(registro)
        registros_acessos.append(registro)

     except ValueError:
            print("Erro: entrada inválida!.")

print(registros_acessos)