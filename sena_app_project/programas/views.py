from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Programa
from django.contrib import messages
from django.views.generic import FormView
from django.views import generic
from programas.forms import ProgramaForm

def programas(request):
    lista_programas = Programa.objects.all().order_by('nombre')
    template = loader.get_template('lista_programas.html')
    contexto = {
        'lista_programas': lista_programas,
        'total_programas': lista_programas.count(),
    }
    
    return HttpResponse(template.render(contexto, request))

class ProgramaFormView(FormView):
    template_name = 'crear_programa.html'
    form_class = ProgramaForm
    success_url = "../programas/"

    def form_valid(self, form):
        # Guardar el programa
        programa = form.save()
        
        # Agregar mensaje de éxito
        messages.success(
            self.request, 
            f'El programa {programa.nombre} - {programa.codigo} ha sido registrado exitosamente.'
        )
        
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, 
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)