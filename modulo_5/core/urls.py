from django.urls import path 
from .views import (
    ListaTarefasAPIView, ContagemTarefasAPIView, 
    TarefaDeleteAPIView, DetalheTarefaAPIView,
    DuplicarTarefaAPIView, ConcluirTodasTarefasAPIView,
    TarefaListCreateAPIView, TarefaRetrieveUpdateDestroyAPIView,
    LogoutView, MeView, ChangePasswordView, StatsView, RegisterView
    )
 
app_name = 'core' 
 
urlpatterns = [ 
    # /api/tarefas/ → ListaTarefasAPIView 
    
# Rotas de Tarefas (CRUD e filtros)
                #CREATE
        path('tarefas/<int:pk>/', DetalheTarefaAPIView.as_view(), name='detalhe_tarefa'),

                #READ
        path('me/', MeView.as_view(), name='me'),
        path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'), 
        path('tarefas/estatisticas/', ContagemTarefasAPIView.as_view(), name='estatisticas-tarefas'),
        path('tarefas/<int:pk>/', DetalheTarefaAPIView.as_view(), name='detalhe-tarefa'),

                #UPDATE
        # Coleção: Lista e Cria
        path('tarefas/', TarefaListCreateAPIView.as_view(), name='tarefa-list-create'),
        # Recurso Individual: Detalhe, Atualiza, Deleta
        path('tarefas/<int:pk>/', TarefaRetrieveUpdateDestroyAPIView.as_view(), name='tarefa-detail'),
        
        path('tarefas/<int:pk>/duplicar/', DuplicarTarefaAPIView.as_view(), name='duplicar-tarefa'),
        path('tarefas/concluir-todas/', ConcluirTodasTarefasAPIView.as_view(), name='concluir-todas'),
        path('change-password/', ChangePasswordView.as_view(), name='change_password'),

                #DELETE
        path('tarefas/<int:pk>/delete/', TarefaDeleteAPIView.as_view(), name='delete-tarefa'),

                #FILTROS
        path('logout/', LogoutView.as_view(), name='logout'),
        path('stats/', StatsView.as_view(), name='stats'),
        path('register/', RegisterView.as_view(), name='register'),

]