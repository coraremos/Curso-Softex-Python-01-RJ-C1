from datetime import datetime

from rest_framework import status, generics
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated, AllowAny, DjangoModelPermissions

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView 

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Tarefa 
from .permissions import IsGerente, CanDeleteTask

from .serializers import (
    TarefaSerializer, 
    CustomTokenObtainPairSerializer, 
    UserRegistrationSerializer,
)


class ListaTarefasAPIView(APIView): 
    """
    View para operações de coleção (GET e POST).
    
    Endpoints:
        GET /api/tarefas/  - Lista todas as tarefas
        POST /api/tarefas/ - Cria uma nova tarefa
    """
     
    def get(self, request, format=None): 
        """Lista todas as tarefas."""
        tarefas = Tarefa.objects.filter(deletada=False)
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        """
        Cria uma nova tarefa.
        
        Args:
            request.data: JSON com dados da tarefa
                {
                    "titulo": "string",
                    "concluida": boolean (opcional, default=False)
                }
        
        Returns:
            201 Created: Tarefa criada com sucesso
            400 Bad Request: Dados inválidos
        """
        serializer = TarefaSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ContagemTarefasAPIView(APIView): 
    def get(self, request): 
        tarefas_ativas = Tarefa.objects.filter(deletada=False)
        total = tarefas_ativas.count() 
        concluidas = tarefas_ativas.filter(concluida=True).count() 
        pendentes = total - concluidas 
        
        taxa_conclusao = (concluidas / total) if total > 0 else 0
         
        return Response({ 
            'total': total, 
            'concluidas': concluidas, 
            'pendentes': pendentes,
            'taxa_conclusao': round(taxa_conclusao, 2)
        })
    
class TarefaDeleteAPIView(APIView):
    """
    URL /api/tarefas/<int:pk>/delete/
    """
    def patch(self, request, pk, format=None):
        tarefa = get_object_or_404(Tarefa, pk=pk)
        
        tarefa.deletada = True
        tarefa.save()
        
        return Response(
            {"message": "Tarefa deletada com sucesso."}, 
            status=status.HTTP_200_OK
        )
        
class DetalheTarefaAPIView(APIView):     
    def get_object(self, pk):
        return get_object_or_404(Tarefa, pk=pk)
    
    def get(self, request, pk, format=None):
        # 1. BUSCAR: Usa método auxiliar (trata 404)         
        tarefa = self.get_object(pk)          
        # 2. SERIALIZAR: Converte objeto único (sem many=True)         
        serializer = TarefaSerializer(tarefa)          
        # 3. RESPONDER: Retorna JSON com status 200         
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):         
        tarefa = self.get_object(pk)          
        serializer = TarefaSerializer(tarefa, data=request.data)         
           
        if serializer.is_valid():            
            serializer.save()              
            return Response(serializer.data, status=status.HTTP_200_OK)          # ERRO: Retornar erros de validação         
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):         
        """         Atualiza tarefa parcialmente (merge).          
        Permite enviar apenas os campos que serão modificados.         
        """         
        # 1. BUSCAR: Obter o objeto existente         
        tarefa = self.get_object(pk)          
        # 2. SERIALIZAR: Passar objeto, novos dados E partial=True         
        serializer = TarefaSerializer(             
            tarefa,             
            data=request.data,             
            partial=True # <--- ESSENCIAL PARA O PATCH         
            )          
        # 3. VALIDAR         
        if serializer.is_valid():             
            # 4. SALVAR (aplica apenas os campos recebidos)             
            serializer.save()              
            # 5. RESPONDER             
            return Response(serializer.data, status=status.HTTP_200_OK)          
        # ERRO         
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):         
        """Remove um recurso específico."""         
        # 1. BUSCAR: Obter o objeto (trata 404 se não existir)         
        tarefa = self.get_object(pk)          
        # 2. DELETAR         
        tarefa.delete()          
        # 3. RESPONDER: 204 No Content (sucesso sem corpo de resposta)         
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def concluida_em(self, request, pk, format=None):
        tarefa = get_object_or_404(Tarefa, pk=pk)
        serializer = TarefaSerializer(             
            tarefa,             
            data=request.data,             
            partial=True # <--- ESSENCIAL PARA O PATCH         
            )
        if tarefa.concluida_em:
            tarefa.save()
            
            return Response(
                {"message": "A tarefa foi concluída em: {data}."}, 
                status=status.HTTP_200_OK
            )
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DuplicarTarefaAPIView(APIView):
    
    def post(self, request, pk, format=None):
        tarefa_original = get_object_or_404(Tarefa, pk=pk)
        
        nova_tarefa = Tarefa(
            user=tarefa_original.user,
            titulo=f"Cópia de {tarefa_original.titulo}", 
            concluida=False, 
            prioridade=tarefa_original.prioridade,
            prazo=tarefa_original.prazo,
            deletada=False,
            concluida_em=None
        )
        
        nova_tarefa.save()
        
        serializer = TarefaSerializer(nova_tarefa)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ConcluirTodasTarefasAPIView(APIView):
    def patch(self, request, format=None):
        tarefas_pendentes = Tarefa.objects.filter(concluida=False, deletada=False)

        now = datetime.now()
        
        quantidade_atualizada = tarefas_pendentes.update(
            concluida=True,
            concluida_em=now
        )
        
        return Response(
            {
                "message": f"{quantidade_atualizada} tarefas foram marcadas como concluídas.", 
                "concluidas": quantidade_atualizada
            }, 
            status=status.HTTP_200_OK
        )
    
class MinhaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(f"Usuário autenticado: {request.user.username}")

class TarefaListCreateAPIView(generics.ListCreateAPIView):
    """
    Lista tarefas e permite a criação de novas tarefas.

    PROTEGIDA: Requer autenticação JWT.
    """
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions] # ← Proteção

    def get_queryset(self):         
        """         
        Sobrescreve o comportamento padrão para retornar APENAS         
        os dados pertencentes ao usuário logado.      

        Fluxo:
        1. JWT decodifica o token → request.user (Objeto User)        
        2. ORM filtra: WHERE user_id = request.user.id        
        3. Retorna QuerySet filtrado        
        """              
        # Retorna o filtro. O Django fará o WHERE user_id = X no banco.         
        return Tarefa.objects.filter(user=self.request.user)     
     
    def perform_create(self, serializer):         
        # Garante que a tarefa criada seja vinculada ao usuário logado         
        serializer.save(user=self.request.user)

class TarefaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    View de detalhe com RBAC implementado.
    
    Regras: 
    - GET, PUT, PATCH: Qualquer usuário autenticado (desde que seja dono)
    - DELETE: Apenas usuários do grupo 'Gerente'
    """

    serializer_class = TarefaSerializer

    def get_queryset(self):         
        """         
                 
        Filtra queryset para APENAS tarefas do usuário logado:
            Garante que operações de detalhe (GET, PUT, DELETE por ID)         
            só encontrem o objeto se ele pertencer ao usuário.

        Segurança:
        - GET /api/tarefas/999/ (tarefa de outro usuário) → 404        
        - DELETE /api/tarefas/999/ → 404
        - PUT /api/tarefas/999/ → 404

        Por que 404 e não 403?        
            403 Forbidden revela que o recurso existe.
            404 Not Found oculta a existência do dado.
        """                
        return Tarefa.objects.filter(user=self.request.user)
    
    def get_permissions(self):     
        """ Versão alternativa usando permissão de negócio. """
        return [IsAuthenticated(), CanDeleteTask()]

        """         
        Instancia e retorna a lista de permissões que esta view requer,         
        dependendo do método HTTP da requisição.         

        Fluxo de verificação: 
        1. Método é DELETE? → Exige IsAuthenticated + IsGerente
        2. Outros métodos? → Apenas IsAuthenticated

        Ordem importa: 
        - Is Authenticated SEMPRE primeiro (garante login).
        - Permissões específicas depois.
        """         
        #if self.request.method == 'DELETE':             
            # Para deletar: Precisa estar logado E ser Gerente             
            # A ordem importa: primeiro checa login, depois o grupo             
            #return [IsAuthenticated(), IsGerente()]     
                     
        # Para GET, PUT, PATCH: Basta estar logado (e ser dono, garantido pelo queryset)        
        #return [IsAuthenticated()]
    
        

class CustomTokenObtainPairView(TokenObtainPairView):
    """View que usa o serializer customizado."""     
    serializer_class = CustomTokenObtainPairSerializer

class LogoutView(APIView):     
    permission_classes = [IsAuthenticated]          
    def post(self, request):         
        try:             
            refresh_token = request.data.get("refresh")             
            token = RefreshToken(refresh_token)             
            token.blacklist()  # Adiciona o token à lista negra                          
            return Response(                 
                {"detail": "Logout realizado com sucesso."},                 
                status=status.HTTP_205_RESET_CONTENT # 205 é a resposta padrão para "reset content"             
            )         
        except Exception: # Captura exceções como token_not_valid             
            return Response(                 
                {"detail": "Token inválido."},                 
                status=status.HTTP_400_BAD_REQUEST             
            )

class MeView(APIView): 
    """ Retorna dados do usuário autenticado 

    endpoint: /api/me/
    """
    permission_classes = [IsAuthenticated] 
     
    def get(self, request): 
        serializer = UserRegistrationSerializer(request.user)
        return Response(serializer.data)

class ChangePasswordView(APIView): 
    """
    Cria endpoint /api/change-password/ protegido
    """
    permission_classes = [IsAuthenticated] 
     
    def post(self, request): 
        user = request.user 
        old_password = request.data.get('old_password') 
        new_password = request.data.get('new_password') 
         
        if not user.check_password(old_password): 
            return Response( 
                {'error': 'Senha atual incorreta'}, 
                status=400 
            ) 
         
        user.set_password(new_password) 
        user.save() 
         
        return Response({'detail': 'Senha alterada com sucesso'})

class StatsView(APIView):
    """
    Endpoint /api/stats/ que retorna estatísticas do usuário autenticado:
    total_tarefas, concluidas, pendentes e taxa_conclusao.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        
        # Filtra tarefas do usuário logado que não foram marcadas como deletadas
        tarefas_do_usuario = Tarefa.objects.filter(user=user, deletada=False)

        # Contagem de tarefas
        total_tarefas = tarefas_do_usuario.count()
        concluidas = tarefas_do_usuario.filter(concluida=True).count()
        pendentes = total_tarefas - concluidas

        # Cálculo da taxa de conclusão (tratando divisão por zero)
        taxa_conclusao = concluidas / total_tarefas if total_tarefas > 0 else 0.0
        
        return Response({
            "total_tarefas": total_tarefas,
            "concluidas": concluidas,
            "pendentes": pendentes,
            # Arredonda a taxa para 2 casas decimais, conforme o exemplo
            "taxa_conclusao": round(taxa_conclusao, 2) 
        })

class RegisterView(generics.CreateAPIView):     
    """     
    Endpoint PÚBLICO para cadastro de novos usuários.

    Segurança:
    - AllowAny: Qualquer um pode criar conta
    - Senha é hasheada automaticamente
    - Email e username devem ser únicos (validação do Django)
        
    Exemplo:
    POST /api/register/
    {
        "username": "novo_usuario",
        "email": "novo@exemplo.com",
        "password": "senha_segura_123",
        "password_confirm": "senha_segura_123"
    }     
    """     
    queryset = User.objects.all()     
    permission_classes = [AllowAny] #  ← CRÍTICO: Acesso público     
    serializer_class = UserRegistrationSerializer

