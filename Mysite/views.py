from django.shortcuts import render
from django.http import HttpResponse

def index_pag(request):
    index = 'Mysite/index.html'
    return render(request, index)

def plantas_pag(request):
    plantas = 'Mysite/plantas.html'
    return render(request, plantas)

def contato_pag(request):
    contato = 'Mysite/contato.html'
    return render(request, contato)