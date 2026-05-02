from django.shortcuts import render
from .models import Imoveis

def index(request):
    lista_imoveis = Imoveis.objects.all()
    return render(request, 'gestao/index.html', {'imoveis': lista_imoveis})

def detalhe_imovel():
    return    

# Create your views here.
