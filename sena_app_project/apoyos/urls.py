from django.urls import path
from . import views

app_name = 'apoyos'

urlpatterns = [
    path('apoyos/', views.apoyos, name='lista_apoyos'),
]