from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Programa

def programas(request):
    lista_programas = Programa.objects.all().order_by('nombre')
    template = loader.get_template('lista_programas.html')
    contexto = {
        'lista_programas': lista_programas,
        'total_programas': lista_programas.count(),
    }
    
    return HttpResponse(template.render(contexto, request))