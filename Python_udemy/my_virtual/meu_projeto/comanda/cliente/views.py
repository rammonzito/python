from django.shortcuts import render

# Create your views here.

def home(request):
    nome = "Ramon"
    return render(request, 'cliente.html', {'nome': nome})