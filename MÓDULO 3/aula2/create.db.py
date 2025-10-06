import sqlite3

#ao se conectar, o Python cria o arquivo do banco se ele não existir
conn = sqlite3.connect('meu banco.db')

print("Banco de dados 'meu banco.db' criado com sucesso!")

#é sempre bom fechar a conexão no final
conn.close()