from django.template import loader
from django.http import HttpResponse
from .models import Apoyos

# Create your views here.

def apoyos(request):
    lista_apoyos = Apoyos.objects.all().order_by('-fecha_asignacion')
    
    template = loader.get_template('lista_apoyos.html')
    context = {
        'lista_apoyos': lista_apoyos,
        'total_apoyos': lista_apoyos.count(),
    }
    return HttpResponse(template.render(context, request))