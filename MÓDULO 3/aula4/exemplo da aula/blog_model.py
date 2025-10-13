import sqlite3
from database import DatabaseConnection
from datetime import datetime
from user_model import UserModel

class BlogModel:

    def __init__(self):
        self.db_conn = DatabaseConnection()
        self._create_table()
    
    def _create_table(self):
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS blogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                conteudo TEXT NOT NULL,
                data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                data_atualizacao DADETIME DEFAULT CURRENT_TIMESTAMP
                id_user INTEGER,
                FOREIGN KEY (id_user) REFERENCES usuarios(id)
            );
"""
)
    def create_post(self, titulo, conteudo, id_user):
        
        self.db_conn.connect()

        self.db_conn.cursor.execute(
            """
            INSERT INTO blogs (titulo, conteudo, id_user)
            VALUES (?,?,?);
        """,
            (titulo, conteudo,id_user),
        )
        print("Postagem criada com sucesso!")
        
        self.db_conn.close()

    def update_post_by_id(self, user_id, titulo=None, conteudo=None):
        self.db_conn.connect()
        updates = []
        params = []
        if titulo:
            updates.append("titulo = ?")
            params.append(titulo)
        if conteudo:
            updates.append("conteudo = ?")
            params.append(conteudo)
        if not updates:
            print("Nenhuma postagem para atualizar.")
            self.db_conn.close()
            return
        
        updates.append("data_atualizacao = ?")
        params.append(datetime.now())
        params.append(user_id)
        query = f"UPDATE blogs SET {', '.join(updates)} WHERE id = ?;"

        self.db_conn.cursor.execute(query, params)
        print("Postagem atualiza com sucesso!")
        self.db_conn.close()

    def delete_post_by_id(self, user_id):
        self.db_conn.connect()
        self.db_conn.cursor.execute("DELETE FROM blogs WHERE id = ?;", (user_id,))
        print("Postagem deletada com sucesso!")
        self.db_conn.close()
    
    def get_all_posts(self):
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM blogs;")
        posts = self.db_conn.cursor.fetchall()
        self.db_conn.close()
        return posts
    
    def get_all_posts_by_user_id(self, user_id):
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM blogs WHERE id_user = ? ;", (user_id,))
        posts = self.db_conn.cursor.fetchall()
        self.db_conn.close()
        return posts
