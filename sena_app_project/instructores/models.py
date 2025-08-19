from django.db import models

# Create your models here.
class Instructor(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('TI', 'Tarjeta de Identidad'),
        ('PAS', 'Pasaporte'),
    ]
    
    NIVEL_EDUCATIVO_CHOICES = [
        ('TEC', 'Técnico'),
        ('TGL', 'Tecnólogo'),
        ('PRE', 'Pregrado'),
        ('ESP', 'Especialización'),
        ('MAE', 'Maestría'),
        ('DOC', 'Doctorado'),
    ]
    
    documento_identidad = models.CharField(max_length=20, unique=True)
    tipo_documento = models.CharField(max_length=3, choices=TIPO_DOCUMENTO_CHOICES, default='CC')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, default='')  # Valor por defecto para evitar error
    telefono = models.CharField(max_length=10, null=True, blank=True)  # Permitir nulos
    email = models.EmailField(null=True, blank=True)  # Permitir nulos
    fecha_nacimiento = models.DateField()
    ciudad = models.CharField(max_length=100, null=True, blank=True)  # Permitir nulos
    direccion = models.TextField(null=True, blank=True)  # Permitir nulos
    nivel_educativo = models.CharField(max_length=3, choices=NIVEL_EDUCATIVO_CHOICES, default='MAE')
    especialidad = models.CharField(max_length=100, default='')  # Valor por defecto
    anos_experiencia = models.PositiveIntegerField(default=0)  # Valor por defecto
    activo = models.BooleanField(default=True)
    fecha_vinculacion = models.DateField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"
    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"