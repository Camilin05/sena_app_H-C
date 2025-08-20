from django.shortcuts import render, get_object_or_404
from .models import Aprendiz, Curso
from instructores.models import Instructor
from programas.models import Programa 
from aprendices.forms import AprendizForm
from django.views import generic


def aprendices(request):
    lista_aprendices = Aprendiz.objects.all().order_by('apellido', 'nombre')
    context = {
        'lista_aprendices': lista_aprendices,
        'total_aprendices': lista_aprendices.count(),
    }
    return render(request, 'lista_aprendices.html', context)

def inicio(request):
    total_aprendices = Aprendiz.objects.count()
    total_instructores = Instructor.objects.count()
    total_programas = Programa.objects.count() 
    cursos_activos = Curso.objects.filter(estado__in=['INI', 'EJE']).count()
    
    context = {
        'total_aprendices': total_aprendices,
        'total_instructores': total_instructores,
        'total_programas': total_programas,
        'cursos_activos': cursos_activos,
    }
    return render(request, 'inicio.html', context)

def lista_cursos(request):
    cursos = Curso.objects.all().order_by('-fecha_inicio')
    context = {
        'lista_cursos': cursos,
        'total_cursos': cursos.count(),
    }
    return render(request, "lista_cursos.html", context)

def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    aprendices_curso = curso.aprendizcurso_set.all()
    instructores_curso = curso.instructorcurso_set.all()
    
    context = {
        'curso': curso,
        'aprendices_curso': aprendices_curso,
        'instructores_curso': instructores_curso,
    }
    return render(request, 'detalle_curso.html', context)

def detalle_aprendiz(request, aprendiz_id):
    aprendiz = get_object_or_404(Aprendiz, id=aprendiz_id)
    context = {
        'aprendiz': aprendiz,
    }
    return render(request, 'detalle_aprendiz.html', context)

class AprendizFormView(generic.FormView):
    template_name = "crear_aprendiz.html"
    form_class = AprendizForm
    success_url = "../aprendices/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)