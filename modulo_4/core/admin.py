from django.contrib import admin

from .models import Tarefa  # 1. Importe seu Model  

# 1. Crie uma classe que herda de admin.ModelAdmin
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'user', 'get_user_email', 'concluida', 'criada_em')
    list_filter = ('concluida', 'user', 'criada_em') 
    #para pesquisar o titulo é interessante inserir campo de busca nos titulos e não display tudo em lista
    search_fields = ('titulo', 'user__username')
    #campo de busca q procura em titulos e user name.

    fieldsets = (        
        ('Informações Principais', {             
            'fields': ('user', 'titulo')         
        }),
        ('Status da Tarefa', {             
            'fields': ('concluida', 'criada_em')         
        }),     
    )

    readonly_fields = ('criada_em',)

    @admin.display(description='Email do Usuário') # Define o título da coluna     
    def get_user_email(self, obj):         
        return obj.user.email

# 2. "Registre" seu Model no site de administração 
admin.site.register(Tarefa, TarefaAdmin)

