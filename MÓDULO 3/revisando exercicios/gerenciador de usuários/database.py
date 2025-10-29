import sqlite3

class DatabaseConnection:
    """
    Gerencia a conexão com o banco de dados SQLite.
    Define a abertura, o fechamento e a persistência(commit).
    """

    def __init__(self, db_name="escola.db"):
        self.db_name = db_name #para chamar a data base
        self.conn = None #conexão inicialmente None
        self.cursor = None #cursor inicialmente None
    
    def connect(self):
        """Abre a conexão com o banco de dados e configura o RowFactory"""
        if self.conn is None: #se o banco estiver desconectado
            self.conn = sqlite3.connect(self.db_name) #conecte
            self.conn.row_factory = sqlite3.Row #conecte
            self.cursor = self.conn.cursor() #conecte

            # ativa a 'foreign keys' no SQLite, essencial para integridade
            self.cursor.execute("PRAGMA foreign_keys = ON;")
    
    def close(self):
        """Fecha a conexão com o banco de dados, salvando as alterações."""
        if self.conn: #se estiver conectado
            self.conn.commit() #salve
            self.conn.close() #feche a conexão
            self.conn = None #mude o status para None
            self.cursor = None #mude o status para None