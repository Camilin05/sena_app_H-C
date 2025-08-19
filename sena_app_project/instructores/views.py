from django.shortcuts import get_object_or_404
from .models import Instructor
from django.http import HttpResponse
from django.template import loader
from instructores.forms import InstructorForm
from django.views import generic
from django.contrib import messages
from django.views.generic import FormView

def instructores(request):
    lista_instructores = Instructor.objects.all().order_by('nombre', 'apellido')
    template = loader.get_template('lista_instructores.html')
    context = {
        'instructores': lista_instructores,
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


# Create your views here.

class InstructorFormView(FormView):
    template_name = 'crear_instructor.html'
    form_class = InstructorForm
    success_url = "../instructores/"

    def form_valid(self, form):
        # Guardar el instructor
        instructor = form.save()
        
        # Agregar mensaje de éxito
        messages.success(
            self.request, 
            f'El instructor {instructor.nombre} {instructor.apellido} ha sido registrado exitosamente.'
        )
        
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, 
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)