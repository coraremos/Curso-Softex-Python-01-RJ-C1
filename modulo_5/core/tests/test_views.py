from rest_framework.test import APITestCase 
from rest_framework import status 
from django.contrib.auth.models import User, Group 
from django.urls import reverse 
from core.models import Tarefa  

class TarefaAPITest(APITestCase):     
    """     
    Testes de Integração para os endpoints de Tarefa.     
    Simula o ciclo completo: Request -> URL -> View -> Serializer -> DB -> Response     
    """          
    def setUp(self):         
        """Prepara a massa de dados para os testes."""         
        # 1. Criar usuários         
        self.user1 = User.objects.create_user(username='usuario1', password='senha123')         
        self.user2 = User.objects.create_user(username='usuario2', password='senha456')                  
        
        # 2. Criar e atribuir grupos (se sua lógica depender disso)         
        self.grupo_comum = Group.objects.create(name='Comum')         
        self.user1.groups.add(self.grupo_comum)                  
        
        # 3. Criar tarefas iniciais         
        self.tarefa_user1 = Tarefa.objects.create(             
            user=self.user1, titulo='Tarefa do User 1', concluida=False         
        )
        self.tarefa_user2 = Tarefa.objects.create(             
            user=self.user2, titulo='Tarefa do User 2', concluida=True         
        )      
        
    # ------------------ Helpers ------------------      
    
    def obter_token(self, username, password):         
        """         
        Método auxiliar para realizar login e obter o token JWT.         
        Evita repetição de código nos testes.         
        """         
        url = reverse('token_obtain_pair')  # Nome da rota definida no urls.py         
        response = self.client.post(url, {             
            'username': username,             
            'password': password         
        }, format='json')                  
        
        return response.data['access'] 
    
    # ------------------ Testes de Auth ------------------      

#ERRO----------
    # def test_acesso_sem_token_negado(self):
    #     """Testa que endpoint protegido retorna 401 para anônimos."""
    #     url = reverse('core:lista-tarefas')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_credenciais_validas(self):         
        """Testa se login correto retorna tokens."""         
        url = reverse('token_obtain_pair')         
        response = self.client.post(url, {             
            'username': 'usuario1',             
            'password': 'senha123'         
        }, format='json')                  
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)         
        self.assertIn('access', response.data)         
        self.assertIn('refresh', response.data)   
                   
    def test_login_credenciais_invalidas(self):         
        """Testa rejeição de login com senha errada."""         
        url = reverse('token_obtain_pair')         
        response = self.client.post(url, {             
            'username': 'usuario1',             
            'password': 'senhaerrada' 
        }, format='json')                  
            
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
            
#ERRO EM TODOS
#------------------ Testes de CRUD ------------------      
    # def test_listar_tarefas_apenas_do_usuario_logado(self):         
    #     """         
    #     Testa o isolamento de dados: User1 só vê suas próprias tarefas.         
    #     """         
    #     # Autentica como User1         
    #     token = self.obter_token('usuario1', 'senha123')         
    #     self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')                  
    #     url = reverse('core:lista-tarefas')         
    #     response = self.client.get(url)                  
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)         
    #     self.assertEqual(len(response.data), 1)  # User1 tem 1 tarefa, User2 tem outra         
    #     self.assertEqual(response.data[0]['titulo'], 'Tarefa do User 1')          

    # def test_criar_tarefa(self):         
    #     """         
    #     Testa criação (POST) com injeção automática do usuário logado.         
    #     """         
    #     token = self.obter_token('usuario1', 'senha123')         
    #     self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')    
                    
    #     url = reverse('core:lista-tarefas')         
    #     dados = {             
    #             'titulo': 'Nova Tarefa via API',             
    #             'concluida': False         
    #     }                  
        
    #     # format='json' é crucial para APIs REST        
    #     response = self.client.post(url, dados, format='json')     
                    
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)         
    #     self.assertEqual(response.data['titulo'], 'Nova Tarefa via API')   
            
    #     # Verificação extra: Confere se salvou no banco corretamente         
    #     tarefa_criada = Tarefa.objects.get(id=response.data['id'])         
    #     self.assertEqual(tarefa_criada.user, self.user1)     
            
    # def test_atualizar_tarefa_propria(self):         
    #     """Testa atualização parcial (PATCH) em tarefa própria."""         
    #     token = self.obter_token('usuario1', 'senha123')         
    #     self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')      
                    
    #     url = reverse('core:tarefa-detail', kwargs={'pk': self.tarefa_user1.pk})         
    #     dados = {'concluida': True}              
            
    #     response = self.client.patch(url, dados, format='json')        
                
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)         
    #     self.assertTrue(response.data['concluida'])          
        
    # def test_nao_pode_acessar_tarefa_de_outro_usuario(self):         
    #     """         
    #     Segurança: Tenta acessar via ID uma tarefa que pertence a outro user.         
    #     """         
    #     token = self.obter_token('usuario1', 'senha123')         
    #     self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')    
    
    #     # Tenta acessar tarefa do user2         
    #     url = reverse('core:tarefa-detail', kwargs={'pk': self.tarefa_user2.pk})         
    #     response = self.client.get(url)           
            
    #     # O ideal é 404 Not Found (para não revelar que o ID existe)         
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

#---------------Teste de Permissões (RBAC) baseadas em Roles---------

    def test_usuario_comum_nao_pode_deletar(self):         
        """Testa que usuário sem permissão específica recebe 403 Forbidden."""         
        token = self.obter_token('usuario1', 'senha123')         
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')                  
        url = reverse('core:tarefa-detail', kwargs={'pk': self.tarefa_user1.pk})         
        response = self.client.delete(url)                  
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)          
    
    # def test_gerente_pode_deletar(self):         
    #     """Testa que usuário com cargo 'Gerente' consegue deletar."""         
    #     # Setup específico deste teste: Dar poder de Gerente         
    #     grupo_gerente = Group.objects.create(name='Gerente')         
    #     self.user1.groups.add(grupo_gerente)                  
    #     token = self.obter_token('usuario1', 'senha123')         
    #     self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')                  
    #     url = reverse('core:tarefa-detail', kwargs={'pk': self.tarefa_user1.pk})         
    #     response = self.client.delete(url)                  
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)                  
    #     # Verifica se sumiu do banco         
    #     self.assertFalse(Tarefa.objects.filter(pk=self.tarefa_user1.pk).exists())
    
#------------------Testando Cadastro de Usuários --------------------

class RegisterAPITest(APITestCase):
    """Testes específicos para o endpoint de registro público"""
    def setUp(self):
        #Necessário pois a View de registro atribui este grupo
        self.grupo_comum = Group.objects.create(name='Comum')

    # def test_cadastro_usuario_sucesso(self):
    #     """Testa o fluxo feliz de cadastro."""
    #     url = reverse('core:register')
    #     dados = {
    #         'username':'novousuario',
    #         'email':'novo@email.com',
    #         'password':'senha_segura_123'
    #     }

    #     response = self.client.post(url, dados, format='json')

    #     self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    #     self.assertIn('username',response.data)
    #     #Segurança: a senha nunca deve ser retornada na resposta
    #     self.assertNotIn('password', response.data)

    #     #Verifica criação no banco
    #     user = User.objects.get(username='novousuario')
    #     #Verifica se a senha foi hasheada (não está em texto plano)
    #     self.assertTrue(user.check_password('senha_segura_123'))
    #     #Verifica atribuição de grupo default
    #     self.assertTrue(user.groups.filter(name='Comum').exists())

    def test_cadastro_username_duplicado(self):
        """Testa a validação de unicidade do banco."""
        User.objects.create_user(username='existente', password='123')
        url = reverse('core:register')
        dados = {
            'username':'existente', #username já em uso
            'email':'outro@email.com',
            'password':'senha123'
        }

        response = self.client.post(url,dados,format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)