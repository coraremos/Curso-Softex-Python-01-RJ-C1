import unittest
from unittest.mock import patch, MagicMock
from user_service import UserService

# Dicionário de um usuário simulado para usar em vários testes
MOCK_USER_DATA = {
    'id': 1,
    'senha_hash': 'hashed_password_abc',
    'email': 'teste@exemplo.com',
    'nome_completo': 'Nome Teste',
    'perfil_acesso': 'Afiliado'
}

# Dicionário do usuário "seguro" (sem a senha_hash)
MOCK_SAFE_USER_DATA = {
    'id': 1,
    'email': 'teste@exemplo.com',
    'nome_completo': 'Nome Teste',
    'perfil_acesso': 'Afiliado'
}


# Usamos o 'patch' para substituir (mockar) a dependência do UserModel
@patch('user_service.UserModel')
# Usamos o 'patch' para substituir (mockar) as funções de hash
@patch('user_service.hash_senha')
@patch('user_service.verificar_senha')
class TestUserService(unittest.TestCase):
    
    # O método setUp é executado antes de CADA método de teste (test_...)
    def setUp(self, MockVerificarSenha, MockHashSenha, MockUserModel):
        # Cria uma instância da classe de serviço para testar
        self.user_service = UserService()
        
        # Armazena as mocks para fácil acesso dentro dos testes
        self.mock_user_model = MockUserModel.return_value
        self.mock_hash_senha = MockHashSenha
        self.mock_verificar_senha = MockVerificarSenha

    ## --- Testes de Cadastro (register_user) ---
    
    def test_register_user_success(self):
        """Testa se o cadastro de um novo usuário funciona com sucesso."""
        
        # 1. Configurar as mocks para simular o comportamento
        self.mock_hash_senha.return_value = 'novo_hash_abc'
        self.mock_user_model.create_user.return_value = (True, "Usuário criado com sucesso!")
        
        # 2. Chamar o método que queremos testar
        success, message = self.user_service.register_user(
            senha="minhasenha123",
            email="novo.usuario@empresa.com",
            nome_completo="Novo Sobrenome",
            perfil="Afiliado"
        )
        
        # 3. Fazer as verificações (Assertions)
        self.assertTrue(success)
        self.assertEqual(message, "Usuário criado com sucesso!")
        
        # Verifica se o método de criação do banco foi chamado com o hash correto
        self.mock_user_model.create_user.assert_called_once_with(
            senha_hash='novo_hash_abc',
            email='novo.usuario@empresa.com',
            nome_completo='Novo Sobrenome',
            perfil_acesso='Afiliado'
        )

    def test_register_user_failure_invalid_email(self):
        """Testa se o cadastro falha com um e-mail inválido (sem '.com')."""
        
        # 1. Dados de teste inválidos
        email_invalido = "email@invalido" 
        
        # 2. Chamar o método
        success, message = self.user_service.register_user(
            senha="minhasenha123",
            email=email_invalido,
            nome_completo="Novo Sobrenome",
            perfil="Afiliado"
        )
        
        # 3. Fazer as verificações (Assertions)
        self.assertFalse(success)
        self.assertIn("email precisa ter o mínimo de 10 caracteres, ter '@' e terminar com '.com'", message)
        
        # Verifica se o método de criação do banco NÃO foi chamado (pois falhou na validação)
        self.mock_user_model.create_user.assert_not_called()

    ## --- Testes de Login (login_user) ---

    def test_login_user_success(self):
        """Testa o login bem-sucedido."""
        
        # 1. Configurar as mocks
        self.mock_user_model.find_user_by_email.return_value = MOCK_USER_DATA
        self.mock_verificar_senha.return_value = True # Senha correta
        
        # 2. Chamar o método
        user, message = self.user_service.login_user('teste@exemplo.com', 'minhasenha')
        
        # 3. Fazer as verificações
        self.assertIsNotNone(user)
        self.assertEqual(message, "Login bem-sucedido!")
        self.assertEqual(user['email'], 'teste@exemplo.com')
        # Verifica se a senha_hash foi removida no _safe_user_data
        self.assertNotIn('senha_hash', user) 
        
        # Verifica se a função de verificação de senha foi chamada
        self.mock_verificar_senha.assert_called_once_with('minhasenha', MOCK_USER_DATA['senha_hash'])

    def test_login_user_failure_wrong_password(self):
        """Testa o login com senha incorreta."""
        
        # 1. Configurar as mocks
        self.mock_user_model.find_user_by_email.return_value = MOCK_USER_DATA
        self.mock_verificar_senha.return_value = False # Senha incorreta
        
        # 2. Chamar o método
        user, message = self.user_service.login_user('teste@exemplo.com', 'senha_errada')
        
        # 3. Fazer as verificações
        self.assertIsNone(user)
        self.assertEqual(message, "Credenciais inválidas.")
        
    ## --- Testes de Atualização de Perfil (update_user_profile) ---
    
    def test_update_user_profile_success_self_edit(self):
        """Testa a atualização do próprio perfil com sucesso."""
        
        # 1. Configurar as mocks
        # Simula o usuário logado (current_user_id=1) tentando editar a si mesmo (target_user_id=1)
        self.mock_user_model.update_user_by_id.return_value = (True, "Usuário atualizado com sucesso!")
        self.mock_hash_senha.return_value = 'novo_hash_da_senha'
        
        new_data = {
            "nome_completo": "Novo Nome",
            "senha": "nova_senha123",
        }
        
        # 2. Chamar o método
        success, message = self.user_service.update_user_profile(
            current_user_id=1,
            current_user_profile="Afiliado",
            target_user_id=1,
            new_data=new_data
        )
        
        # 3. Fazer as verificações
        self.assertTrue(success)
        self.assertEqual(message, "Usuário atualizado com sucesso!")
        
        # Verifica os dados que foram passados para o UserModel
        self.mock_user_model.update_user_by_id.assert_called_once()
        args, _ = self.mock_user_model.update_user_by_id.call_args
        
        self.assertEqual(args[0], 1) # target_user_id
        # Verifica se o nome e o hash da senha foram passados para o update
        self.assertEqual(args[1]['nome_completo'], 'Novo Nome')
        self.assertEqual(args[1]['senha_hash'], 'novo_hash_da_senha')

    def test_update_user_profile_failure_unauthorized(self):
        """Testa a falha na atualização quando o usuário não está autorizado."""
        
        # Usuário Afiliado (id=2) tentando editar o usuário 1
        current_user_id = 2
        target_user_id = 1
        
        # 2. Chamar o método
        success, message = self.user_service.update_user_profile(
            current_user_id=current_user_id,
            current_user_profile="Afiliado",
            target_user_id=target_user_id,
            new_data={"nome_completo": "Nome Malicioso"}
        )
        
        # 3. Fazer as verificações
        self.assertFalse(success)
        self.assertEqual(message, "Acesso Negado!")
        self.mock_user_model.update_user_by_id.assert_not_called()

    ## --- Testes de Deleção (delete_user) ---
    
    def test_delete_user_success_diretoria(self):
        """Testa a deleção de um usuário por um perfil 'Diretoria'."""
        
        # 1. Configurar a mock: simula a deleção com sucesso
        self.mock_user_model.delete_user_by_id.return_value = (True, "Usuário deletado com sucesso!")
        
        # 2. Chamar o método
        success, message = self.user_service.delete_user(
            current_user_profile="Diretoria",
            user_id=99
        )
        
        # 3. Fazer as verificações
        self.assertTrue(success)
        self.assertEqual(message, "Usuário deletado com sucesso.")
        self.mock_user_model.delete_user_by_id.assert_called_once_with(99)

    def test_delete_user_failure_unauthorized_profile(self):
        """Testa a falha na deleção quando o perfil não é 'Diretoria'."""
        
        # 1. Não precisa configurar a mock, pois falhará antes de chamar o modelo
        
        # 2. Chamar o método
        success, message = self.user_service.delete_user(
            current_user_profile="Associado",
            user_id=99
        )
        
        # 3. Fazer as verificações
        self.assertFalse(success)
        self.assertEqual(message, "Acesso negado: apenas usuários com perfil 'Diretoria' podem deletar usuários.")
        self.mock_user_model.delete_user_by_id.assert_not_called()

if __name__ == '__main__':
    # Para executar os testes
    unittest.main()