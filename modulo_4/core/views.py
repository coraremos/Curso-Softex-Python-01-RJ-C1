from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Tarefa  # 1. Importe o Model Tarefa
from .forms import TarefaForm
#from django.http import HttpResponse

#uma view é uma função que recebe um 'request' e retorna uma 'response'
@login_required
def home(request):

    # 3. Lógica de POST: Se o formulário foi enviado     
    if request.method == 'POST':         
     # Cria uma instância do form e preenche com os dados do POST
        form = TarefaForm(request.POST)
    
        # 4. O Django valida os dados (max_length, etc.)         
        if form.is_valid():    

            # 'commit=False' cría o objeto na memória, mas não salva no banco. 
            tarefa = form.save(commit=False) 
            # Atribui o usuário logado (request.user) ao campo 'user' da tarefa 
            tarefa.user = request.user 

            # 5. Salva o objeto completo no banco de dados!             
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
    todas_as_tarefas = Tarefa.objects.filter(user=request.user).all().order_by('-criada_em') 
    # Filtre apenas onde o campo 'user' é igual ao 'request.user' / Ordena pelas mais novas
    
    #vamos retornar a resposta HTTP mais simples: um texto HTML
    # return HttpResponse("<h1>Olá, Mundo! Esta é a primeira página Django da Corar!</h1>")
    context = {
        'nome_usuario': request.user.username, # Use o nome do usuário logado! 
        'tecnologias': ['Autenticação', 'ForeignKey', 'Login'],
        'tarefas': todas_as_tarefas,  # 4. Adicione as tarefas ao contexto
        'form': form,
    }

    return render(request,'home.html',context)

@login_required 
def concluir_tarefa(request, pk):     

    # 1. Busca a tarefa pela 'pk' (ID) vinda da URL | E ONDE o 'user' é o 'request.user'    
    # Se não achar, retorna um erro 404.     
    tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)   

    # 2. Segurança: Apenas execute se o método for POST     
    if request.method == 'POST':         
        # 3. A Lógica de "Update"         
        tarefa.concluida = True         
        tarefa.save() # Não se esqueça de salvar!                  
    
        # 4. Redireciona de volta para a 'home' (Padrão PRG)         
        return redirect('home')  

@login_required 
def deletar_tarefa(request, pk):     
    # 1. Busca a tarefa     
    tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)     

    # 2. Segurança: Apenas execute se o método for POST     
    if request.method == 'POST':      
        # 3. A Lógica de "Delete"        
        tarefa.delete()          

        # 4. Redireciona de volta para a 'home'         
        return redirect('home')

def register(request): 
    # Se a requisição for POST, o usuário enviou o formulário 
    if request.method == 'POST': 

        # Cria uma instância do formulário com os dados enviados 
        form = UserCreationForm(request.POST) 

        # Verifica se o formulário é válido (ex: senhas batem, username não existe) 
        if form.is_valid(): 
            user = form.save() # Salva o novo usuário no banco 
            login(request, user) # Faz o login automático do usuário 
            return redirect('home') # Redireciona para a home 
        
    # Se a requisição for GET, o usuário apenas visitou a página 
    else: 
        form = UserCreationForm() # Cria um formulário de cadastro vazio 
     
    # Prepara o contexto e renderiza o template 
    context = {'form': form} 
    return render(request, 'register.html', context)
