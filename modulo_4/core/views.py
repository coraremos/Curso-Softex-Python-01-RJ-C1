from django.shortcuts import render, redirect
from .models import Tarefa  # 1. Importe o Model Tarefa
from .forms import TarefaForm
#from django.http import HttpResponse

#uma view é uma função que recebe um 'request' e retorna uma 'response'
def home(request):

    # 3. Lógica de POST: Se o formulário foi enviado     
    if request.method == 'POST':         
     # Cria uma instância do form e preenche com os dados do POST
        form = TarefaForm(request.POST)
    
        # 4. O Django valida os dados (max_length, etc.)         
        if form.is_valid():             
            # 5. Salva o objeto no banco de dados!             
            form.save()

            # 6. Redireciona de volta para a 'home'             
            # Isso é o Padrão "Post-Redirect-Get" (PRG)             
            return redirect('home')

         # Se o form NÃO for válido, o código continua e          
         # o 'form' (com os erros) será enviado para o template
   
    # 7. Lógica de GET: Se o usuário apenas visitou a página     
    else:         
        form = TarefaForm()  # Cria um formulário vazio
    # 2. Use o ORM para buscar os dados!     
    # Tarefa.objects.all() significa: "Pegue todas as linhas da tabela Tarefa"    
    # 8. A busca de dados (fora dos 'ifs', pois é necessária sempre)
    todas_as_tarefas = Tarefa.objects.all().order_by('-criada_em') # Ordena pelas mais novas
    
    #vamos retornar a resposta HTTP mais simples: um texto HTML
    # return HttpResponse("<h1>Olá, Mundo! Esta é a primeira página Django da Corar!</h1>")
    context = {
        'nome_usuario':'Júnior',
        'tecnologias':['Python','Django','HTML','CSS'],
        'tarefas': todas_as_tarefas,  # 4. Adicione as tarefas ao contexto
        'form': form,
    }



    return render(request,'home.html',context)

