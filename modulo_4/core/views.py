from django.shortcuts import render
from .models import Tarefa  # 1. Importe o Model Tarefa
# Create your views here.
from django.http import HttpResponse

#uma view é uma função que recebe um 'request' e retorna uma 'response'
def home(request):
   
    # 2. Use o ORM para buscar os dados!     
    # Tarefa.objects.all() significa: "Pegue todas as linhas da tabela Tarefa"    
    todas_as_tarefas = Tarefa.objects.all()
    
    #vamos retornar a resposta HTTP mais simples: um texto HTML
    # return HttpResponse("<h1>Olá, Mundo! Esta é a primeira página Django da Corar!</h1>")
    context = {
        'nome_usuario':'Júnior',
        'tecnologias':['Python','Django','HTML','CSS'],
        'tarefas': todas_as_tarefas  # 4. Adicione as tarefas ao contexto
    }



    return render(request,'home.html',context)

