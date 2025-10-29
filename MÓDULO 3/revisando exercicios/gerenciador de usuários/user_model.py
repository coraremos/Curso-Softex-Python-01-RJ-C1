import sqlite3
from datetime import datetime
from database import DatabaseConnection

class UserModel:

    def __init__(self):
        self.db_conn = DatabaseConnection()
        self._create_table()

    def _create_table(self):
        """Cria tabela de usuários simplificada (apenas login, nome e perfil)"""
        self.db_conn.connect()
        self.db_conn.cursor.execute( #permitira nessa tabela conexão com foreign key
            """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY ATOINCREMENT,
                senha_hash TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                nome_completo TEXT,
                perfil_acesso TEXT DEFAULT CURRENT_TIMESTAMP,
                data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        """
        )
        self.db_conn.close()
    
    def create_user(
        self, 
        senha_hash:str, 
        email:str, 
        nome_completo:str, 
        perfil_acesso:str
    ) -> tuple[bool, str]:
        """Cria um novo usuário, 
        usando colunas e placeholders(espaços reservados) explícitos"""

        self.db_conn.connect()

        # define os valores em palavras-chave:
        field_names = "email, senha_hash, nome_completo, perfil_acesso"
        placeholders = "?, ?, ?, ?"
        params = (email, senha_hash, nome_completo, perfil_acesso,) #em tupla

        try: #o try depende de um fechamento except, não o esquecer!
            self.db_conn.cursor.execute(
                f"""
                INSERT INTO usuarios ({field_names}) VALUES ({placeholders});
            """,
                params,
            )

            self.db_conn.close()
            return True, "Usuário criado com sucesso!"
        
        except sqlite3.IntegrityError as e: #torna o termo completo em uma palavra chave
            self.db_conn.close()
            if "email" in str(e): #p/ UNIQUE
                return False, f"Erro: o e-mail '{email}' já está em uso."
            return False, f"Erro de integridade ao criar usuário: {e}" #p/ NOT NULL
        except Exception as e:
            self.db_conn.close()
            return False, f"Erro desconhecido: {e}"
        
    def find_user_by_id(self, user_id:int):
        """Busca usuário pelo ID"""
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM usuarios WHERE id = ?;", (user_id,))
        user = self.db_conn.cursor.fetchone()
        self.db_conn.close()
        return user
    
    def find_user_by_email(self, email:str):
        """Busca um usuário pelo e-mail (usado no login)"""
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM usuarios WHERE email = ?;", (email,))
        user = self.db_conn.cursor.fetchone()
        self.db_conn.close()
        return user
    
    def update_user_by_id(
            self, 
            user_id: int,
            updates_data: dict,
    ) -> tuple[bool, str]:
        """
        Atualiza informações de um usuário de forma simplificada.
        A query(consulta) é construída dinamicamente no SET(definição) 
        para garantir a flexibilidade de quais campos atualizar.
        """
        