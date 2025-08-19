from django.urls import path
from . import views

app_name = 'programas'

urlpatterns = [
    path('programas/', views.programas, name='lista_programas'),
    path('crear_programa/', views.ProgramaFormView.as_view(), name='crear_programa'),
]