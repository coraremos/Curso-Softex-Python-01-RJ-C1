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
        
        """Recebe um usuário do banco e retorna-o sem a senha."""
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
        """Verifica o perfil do usuário para autorizar ações."""
        if current_user_profile == 'Diretoria':
            return True
        if target_user_id is None:
            return False
        if action == "edit_self":
            return current_user_id == target_user_id
        else:
            False
        
    def _validate_user_data(self, data: dict, is_full_validation: bool = False) -> tuple[bool, str]:
        """
        Método unificado de validação de dados do usuário.
        
        Args:
            data: Dicionário contendo os dados a serem validados (pode incluir senha, email, nome_completo).
            is_full_validation: Se True, exige que todos os campos obrigatórios para cadastro estejam presentes.
                                Usado em register_user.
        """
        senha = data.get('senha')
        email = data.get('email')
        nome_completo = data.get('nome_completo')

        # --- 1. Validações de Senha ---
        # A senha é obrigatória no registro (full validation), mas opcional na atualização
        if senha is not None:
            if len(senha) < 8:
                return False, "A senha deve ter no mínimo 8 caracteres."
        elif is_full_validation: # A senha deve ser fornecida se for um registro
            return False, "A senha é obrigatória para o cadastro."

        # --- 2. Validações de Email ---
        # O email é obrigatório no registro (full validation), mas opcional na atualização
        if email is not None:
            if len(email) < 10 or '@' not in email or not email.endswith('.com'):
                return False, "O email precisa ter o mínimo de 10 caracteres, ter '@' e terminar com '.com'."
        elif is_full_validation: # O email deve ser fornecido se for um registro
            return False, "O email é obrigatório para o cadastro."

        # --- 3. Validações de Nome Completo ---
        # O nome é obrigatório no registro (full validation), mas opcional na atualização
        if nome_completo is not None:
            # Não vazio
            if not nome_completo.strip():
                return False, "O nome não pode estar vazio."

            # Pelo menos um sobrenome
            if len(nome_completo.strip().split()) < 2:
                return False, "O nome completo deve conter nome e pelo menos um sobrenome."
                
            # Apenas letras, espaços e hífens
            nome_sem_separadores = nome_completo.replace(' ', '').replace('-', '')
            if not nome_sem_separadores.isalpha():
                return False, "O nome completo deve conter apenas letras, espaços e hífens."
        elif is_full_validation: # O nome deve ser fornecido se for um registro
             return False, "O nome completo é obrigatório para o cadastro."

        return True, "Dados válidos."

    def register_user(
        self,
        senha: str,
        email: str,
        nome_completo: str,
        perfil: str = "Afiliado",
    ) -> tuple[bool, str]:
        """
        Método para criar um usuário.
        """
        data = {
            'senha': senha,
            'email': email,
            'nome_completo': nome_completo
        }
        
        # Chama a validação completa
        success, message = self._validate_user_data(data, is_full_validation=True)
        if not success:
            return False, message

        senha_hashed = hash_senha(senha)
        
        return self.user_model.create_user(
            senha_hash=senha_hashed, 
            email=email, 
            nome_completo=nome_completo, 
            perfil_acesso=perfil
        )
            
    

    def login_user(self, email: str, senha: str) -> tuple[dict | None, str]:
        """Realiza o login do usuário."""
        if not email or not senha:
            return None, "Falta informação nos campos: ambos precisam ser preenchidos."
        
        user = self.user_model.find_user_by_email(email) 
        
        if not user:
            return None, "Usuário não encontrado."
            
        senha_hash = user['senha_hash']

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
        Método para atualizar usuários, usando a validação unificada.
        """
        if not self._is_authorized(current_user_id, current_user_profile, target_user_id, action="edit_self"):
            return  False, "Acesso Negado!"
        
        # Chama a validação para os dados presentes. Não é validação completa (is_full_validation=False)
        success, message = self._validate_user_data(new_data, is_full_validation=False)
        if not success:
            return False, message

        update_data = {}

        # Mapeia e hasheia os dados validados
        if 'nome_completo' in new_data:
            update_data['nome_completo'] = new_data['nome_completo']
            
        if 'email' in new_data:
            update_data['email'] = new_data['email']

        if 'senha' in new_data:
            # Já validado que a senha existe e é válida, agora hasheia
            update_data['senha_hash'] = hash_senha(new_data['senha']) 
            
        if not update_data:
            return False, "Nenhum dado válido para atualizar."

        # O update_user_by_id espera o dicionário de updates(update_data) + o id
        return self.user_model.update_user_by_id(target_user_id, update_data)

    def delete_user(
        self,
        current_user_profile: str,
        user_id: int,
    ) -> tuple[bool, str]:
        
        """Método para deletar usuarios."""
        if current_user_profile != "Diretoria":
            return False, "Acesso negado: apenas usuários com perfil 'Diretoria' podem deletar usuários."

        if not isinstance(user_id, int) or user_id <= 0:
            return False, "ID de usuário inválido."

        try:
            deleted = self.user_model.delete_user_by_id(user_id)  
        except Exception as e:
            return False, f"Erro ao deletar usuário: {e}"

        if deleted:
            return True, "Usuário deletado com sucesso."
        return False, "Usuário não encontrado."



    def get_user_by_id(self, user_id: int) -> dict | None:

        """Método para pegar um usuário pelo id."""
        if not isinstance(user_id, int) or user_id <= 0:
            return None

        try:
            user = self.user_model.find_user_by_id(user_id)
        except Exception:
            return None

        if not user:
            return None

        return self._safe_user_data(user)
    


    def get_all_users(self) -> list[dict | None]:
        """Método para retornar todos os usuários."""
        try:
            usuarios_brutos = self.user_model.get_all_users()
        except Exception:
            return []

        usuarios_tratados = []
        for user in usuarios_brutos:
            safe = self._safe_user_data(user)
            if safe is not None:
                usuarios_tratados.append(safe)
        return usuarios_tratados
