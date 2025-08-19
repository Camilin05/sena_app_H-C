# apoyos/models.py
from django.db import models

class Apoyos(models.Model):
    TIPO_APOYO_CHOICES = [
        ('ASR', 'Apoyo Sostenimiento Regular'),
        ('FIC', 'Apoyo Sostenimiento FIC'),
        ('ATR', 'Apoyo de transporte'),
        ('ALM', 'Apoyo Alimentación'),
        ('NA', 'No aplica/no tiene'),
    ]
    
    aprendiz = models.ForeignKey(
        "aprendices.Aprendiz", 
        verbose_name="Aprendiz", 
        on_delete=models.CASCADE,
        related_name='apoyos_recibidos'
    )
    tipo_apoyo = models.CharField(
        max_length=3, 
        choices=TIPO_APOYO_CHOICES, 
        verbose_name="Tipo de Apoyo"
    )
    fecha_asignacion = models.DateField(
        auto_now_add=True, 
        verbose_name="Fecha de Asignación"
    )
    monto = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True,
        verbose_name="Monto del Apoyo"
    )
    activo = models.BooleanField(
        default=True, 
        verbose_name="Estado Activo"
    )
    observaciones = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Observaciones"
    )
    
    class Meta:
        verbose_name = "Apoyo"
        verbose_name_plural = "Apoyos"
        ordering = ['-fecha_asignacion']
        unique_together = ['aprendiz', 'tipo_apoyo']  # Un aprendiz no puede tener el mismo tipo de apoyo duplicado
    
    def __str__(self):
        return f"{self.aprendiz.nombre_completo()} - {self.get_tipo_apoyo_display()}"
    
    def get_tipo_apoyo_display_short(self):
        return self.get_tipo_apoyo_display()