from django.shortcuts import render
from django.http import HttpResponse
from .models import Transacao
from .form import TransacaoForm
import datetime

def home(request):
    data = {}
    data['transacoes'] = ['1','2','3']
    data['now'] = datetime.datetime.now()
    # html = str.format("<html><body>It's now {0}</body></html>", now)
    # return HttpResponse(html)
    return render(request, 'contas/home.html', data)
# Create your views here.

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    data = {}
    form = TransacaoForm()
    form = []
    data['form'] = form
    return render(request, 'contas/form.html', data)
