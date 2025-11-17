from django.urls import path
from . import views #O ponto importa as views do app atual

urlpatterns = [
    #Quando a URL for a raiz (''), chame a função 'home' de views.py
    path('',views.home, name='home'),

    # <int:pk> captura um inteiro da URL e o passa para a view como um argumento chamado 'pk'
    path('tarefa/<int:pk>/concluir/', views.concluir_tarefa, name='concluir_tarefa'),
    path('tarefa/<int:pk>/deletar/', views.deletar_tarefa, name='deletar_tarefa'),
]


#   <int:pk>: Esta é a sintaxe do Django para capturar partes de uma URL.  
#             int significa queele espera um número inteiro, 
#             e pk é o nome da variável que será passada para a nossa view. 
