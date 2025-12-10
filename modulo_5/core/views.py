from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from django.shortcuts import get_object_or_404
from .models import Tarefa 
from .serializers import TarefaSerializer 
 
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
    
    