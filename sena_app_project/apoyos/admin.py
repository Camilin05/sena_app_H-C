from django.contrib import admin
from .models import Apoyos

@admin.register(Apoyos)
class ApoyosAdmin(admin.ModelAdmin):
    list_display = (
        'aprendiz',
        'tipo_apoyo',
        'monto',
        'activo',
        'fecha_asignacion',
    )
    
    search_fields = (
        'aprendiz__nombre_completo',
        'aprendiz__documento_identidad',
        'tipo_apoyo',
    )

    list_filter = (
        'tipo_apoyo',
        'activo',
        'fecha_asignacion',
    )
    
    list_editable = (
        'activo',
    )
    
    ordering = ('-fecha_asignacion',)