import pytest
from user_service import UserService

"""
A chave é usar a biblioteca mock 
para simular os métodos do UserModel 
e garantir que o UserService se comporte conforme o esperado, 
sem tocar no banco de dados real.
"""

# userservice = UserService()

# @pytest.mark.parametrize('id', 'senha_hash', 'email', 'nome_completo', 'perfil_acesso', [
#     (1, 'senhaum01', 'user_um@mail.com', 'Usuário Um', 'Diretoria'), #teste para acessos diretoria
#     (2, 'senhadois02', 'user_dois@mail.com', 'Usuário Dois', 'Associado'), #teste geral
#     (3, 'senhatres03', 'user_tres@mail.com', 'Usuário Tres', 'Associado'), #teste update
#     () #teste None            
# ])


def test_safe_user_data():
    pass

def test_is_authorized():
     pass
        
def test_register_use():
     pass  

def test_login_user():
     pass
        
def test_update_user_profile():
     pass
        
def test_delete_user():
     pass
     # with pytest.raises(Exception) as erro_info:
     #      userservice.delete_user()
     # print(erro_info.value)
        
def test_get_user_by_id():
     pass

def test_get_all_users():
     pass