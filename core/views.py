from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#uma view é uma função que recebe um 'request' e retorna uma 'response'
def home(request):
    #vamos retornar a resposta HTTP mais simples: um texto HTML
    return HttpResponse("<h1>Olá, Mundo! Esta é a primeira página Django da Corar!</h1>")

