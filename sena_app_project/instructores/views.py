from django.shortcuts import get_object_or_404
from .models import Instructor
from django.http import HttpResponse
from django.template import loader

def instructores(request):
    lista_instructores = Instructor.objects.all().order_by('nombre', 'apellido')
    
    template = loader.get_template('lista_instructores.html')
    context = {
        'lista_instructores': lista_instructores,
        'total_instructores': lista_instructores.count(),
    }
    return HttpResponse(template.render(context, request))


def detalle_instructor(request, instructor_id):
    instructor = get_object_or_404(Instructor, id=instructor_id)
    template = loader.get_template('detalle_instructor.html')
    cursos_coordinados = instructor.cursos_coordinados.all()
    cursos_impartidos = instructor.cursos_impartidos.all()
    
    context = {
        'instructor': instructor,
        'cursos_coordinados': cursos_coordinados,
        'cursos_impartidos': cursos_impartidos,
    }
    
    return HttpResponse(template.render(request, context))

from .models import Instructor
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404

# Create your views here.

