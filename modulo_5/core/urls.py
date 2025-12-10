from django.urls import path 
from .views import ListaTarefasAPIView, ContagemTarefasAPIView, TarefaDeleteAPIView
 
# Namespace do app (útil para reverse()) 
app_name = 'core' 
 
urlpatterns = [ 
    # /api/tarefas/ → ListaTarefasAPIView 
    path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'), 
    path('tarefas/estatisticas/', ContagemTarefasAPIView.as_view(), name='estatisticas-tarefas'),
    path('tarefas/<int:pk>/delete/', TarefaDeleteAPIView.as_view(), name='delete-tarefa'),
]