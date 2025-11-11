from django.contrib import admin

from .models import Tarefa  # 1. Importe seu Model  

# 2. "Registre" seu Model no site de administração 
admin.site.register(Tarefa)
