from django.shortcuts import render

# Create your views here.

def produto(request):
    nome = "Ramon"
    return render(request, 'produto.html', {'nome': nome})