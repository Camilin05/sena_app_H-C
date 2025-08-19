from django.urls import path
from . import views

urlpatterns = [
    path('apoyos/', views.apoyos, name='apoyos'),
]