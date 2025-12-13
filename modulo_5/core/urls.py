from django.urls import path 
from .views import (
    ListaTarefasAPIView, ContagemTarefasAPIView, 
    TarefaDeleteAPIView, DetalheTarefaAPIView,
    DuplicarTarefaAPIView, ConcluirTodasTarefasAPIView
    )
 
app_name = 'core' 
 
urlpatterns = [ 
    # /api/tarefas/ → ListaTarefasAPIView 
    path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'), 
    path('tarefas/estatisticas/', ContagemTarefasAPIView.as_view(), name='estatisticas-tarefas'),
    path('tarefas/<int:pk>/delete/', TarefaDeleteAPIView.as_view(), name='delete-tarefa'),
    path('tarefas/<int:pk>/', DetalheTarefaAPIView.as_view(), name='detalhe-tarefa'),
    path('tarefas/<int:pk>/duplicar/', DuplicarTarefaAPIView.as_view(), name='duplicar-tarefa'),
    path('tarefas/concluir-todas/', ConcluirTodasTarefasAPIView.as_view(), name='concluir-todas')
]