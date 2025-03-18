from django.shortcuts import render, get_object_or_404
from .models import Contato

def home(request):
    return render(request, 'contatos/home.html')

def lista_contatos(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/lista_contatos.html', {'contatos': contatos})

def detalhes_contato(request, id):
    contato = get_object_or_404(Contato, id=id)
    return render(request, 'contatos/detalhes_contato.html', {'contato': contato})