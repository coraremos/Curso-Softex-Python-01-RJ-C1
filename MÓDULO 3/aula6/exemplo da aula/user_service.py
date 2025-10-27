# user_service.py
from user_model import UserModel
from hasher import hash_senha, verificar_senha
from database import DatabaseConnection


class UserService:
    def __init__(self):
        self.user_model = UserModel()
        """
        crie um atributo que receberá a UserModel como composição
        """

    def _safe_user_data(self, user) -> dict | None:
        
        """
        este é um método privado que recebe um usuarios do banco.
        verifique se o usuários existe e então retorne ele sem a sua senha
        caso ele não exista retorne None
        """
        if user is None:
            return None
        user_dict = dict(user)
        user_dict.pop('senha_hash', None)
        return user_dict
        


    def _is_authorized(
        self,
        current_user_id: int | None,
        current_user_profile: str,
        target_user_id: int,
        action: str,
    ) -> bool:
        
        """
        Método que verifica o perfil do usuários, se for Diretoria retorne true
        Se não tiver target_user_id retorn false
        Se  action == "edit_self" retorne current_user_id == target_user_id
        No geral retorn false
        """
        if current_user_profile == 'Diretoria':
            return True
        if target_user_id is None:
            return False
        if action == "edit_self":
            return current_user_id == target_user_id
        else:
            False
        


    def register_user(
        self,
        senha: str,
        email: str,
        nome_completo: str,
        perfil: str = "Afiliado",
    ) -> tuple[bool, str]:
        
        """
        Método para criar um usuários.
        o campo senha deve ter no mínimo 8 caracteres, caso contrário retorne False a mensagem de erro.
        O campo email deve ter pelo menos 10 caracteres, uma @ e terminar com .com, retorne False se não tiver e a mensagem de erro.
        O campo Nome deve ter apenas letras e não deve estar vazio, retorne False se não tiver e a mensagem de erro.
        Caso os campos atendas as requisições, faça o hash da senha e salve use o método create_user da User Model
        """
        if len(senha) < 8:
            return False, "A senha deve ter no mínimo 8 caracteres."
        if len(email) < 10 or '@' not in email or not email.endswith('.com'):
            return False, "O email precisa ter o mínimo de 10 caracteres, ter '@' e terminar com '.com'."
        if not nome_completo.isalpha():
            return False, "nome só deve ter letras"
        senha_hashed = hash_senha(senha)
        return self.user_model.create_user(nome=nome_completo, email=email, senha_hash=senha_hashed, perfil_acesso=perfil)
            


    def login_user(self, email: str, senha: str) -> tuple[dict | None, str]:

        """
        Este método é o login do usuários, deve receber um email e senha não vazios
        Use o método do find_user_by_email para buscar o usuario
        Se houver usuarios faça a comparação da senha passada com a senha hash do DB
        Use a função verificar_senha, se tiver ok, retorn o usuarios pelo método privado _safe_user_data
        e a mensagem Login bem-sucedido!.
        Caso contrario retorne None e a mensagem de erro
        """
        if not email or not senha:
            return None, "Falta informação nos campos: ambos precisam ser preenchidos."
        
        user = UserModel
        if self.find_user_by_email(user) and senha == hash_senha:
            return True
        user = self.user_model.find_by_email(email)
        if not user:
            return None, "Usuário não encontrado."
        senha_hash = user.get("senha_hash") if isinstance(user, dict) else getattr(user, "senha_hash", None)

        if not verificar_senha(senha, senha_hash):
            return None, "Credenciais inválidas."
        return self._safe_user_data(user), "Login bem-sucedido!"
    


    def update_user_profile(
        self,
        current_user_id: int | None,
        current_user_profile: str,
        target_user_id: int,
        new_data: dict,
    ) -> tuple[bool, str]:
        
        """
        Método para atualizar usuários.
        Chame o método privado _is_authorized, se o retorno for false, retorne false e acesso negado
        Confira as chaves em new_data (senha, nome_completo, email), se pelo menos um desses campos,
        Caso não haja nenhum valor a ser atualizado, encerre a função com False e mensagem de erro.
        Caso contrátio, chame o método da UserModel update_user_by_id passando o id e o new data
        """
        if not self._is_authorized(current_user_id, current_user_profile, target_user_id):
            return  False, "Acesso Negado!"
        
        update_data = {}

        if new_data.get('senha'):
            update_data['senha'] = hash_senha(new_data['senha'])

        if update_data:
            return self.user_model.update_user_by_id(target_user_id, update_data)
        return False, "Nada para atualizar"
    
        

    def delete_user(
        self,
        current_user_profile: str,
        user_id: int,
    ) -> tuple[bool, str]:
        
        """
        Método para deletar usuarios.
        So é permitido deletar usuarios se o current_user_profile for Diretoria.
        Caso não seja retorn false e a mensagem de acesso negado
        Senão chame o método delete_user_by_id, passando o id do usuários
        """
        if not isinstance(current_user_profile, str) or current_user_profile.strip().lower() != "diretoria":
            return False, "Acesso negado: apenas usuários com perfil 'Diretoria' podem deletar usuários."

        if not isinstance(user_id, int) or user_id <= 0:
            return False, "ID de usuário inválido."

        try:
            deleted = self.user_model.delete_user_by_id(user_id)  # ajuste conforme sua API
        except Exception as e:
            return False, f"Erro ao deletar usuário: {e}"

        if deleted:
            return True, "Usuário deletado com sucesso."
        return False, "Usuário não encontrado."



    def get_user_by_id(self, user_id: int) -> dict | None:

        """
        Método para pegar um usuarios pelo id
        Retorne o usuarios apos passar pelo método _safe_user_data
        """
        if not isinstance(user_id, int) or user_id <= 0:
            return None

        try:
            user = self.user_model.find_by_id(user_id)  # ajuste conforme sua API
        except Exception:
            return None

        if not user:
            return None

        return self._safe_user_data(user)
    


    def get_all_users(self) -> list[dict | None]:
        """
        Método para retornar todos os usuários.
        retorne todos os usuáriso apos passar pelo método _safe_user_data
        """
        try:
            raw_users = self.user_model.find_all()  # ajuste conforme sua API
        except Exception:
            return []

        sanitized = []
        for user in raw_users:
            safe = self._safe_user_data(user)
            if safe is not None:
                sanitized.append(safe)
        return sanitized
