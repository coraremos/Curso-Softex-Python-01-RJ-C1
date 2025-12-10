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