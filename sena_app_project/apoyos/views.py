from django.template import loader
from django.http import HttpResponse

# Create your views here.

def apoyos(request):
    lista_apoyos = apoyos.objects.all().order_by('nombre', 'apellido')
    
    template = loader.get_template('lista_apoyos.html')
    context = {
        'lista_apoyos': lista_apoyos,
        'total_apoyos': lista_apoyos.count(),
    }
    return HttpResponse(template.render(context, request))