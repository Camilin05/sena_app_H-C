from django import forms
from .models import Programa

class ProgramaForm(forms.Form):
    codigo = forms.CharField(max_length=20, label="Código del Programa", help_text="Ingrese el número del código.")
    nombre = forms.CharField(max_length=200, label="Nombre del Programa", help_text="Ingrese el nombre del programa.")
    nivel_formacion = forms.ChoiceField( choices=Programa.NIVEL_FORMACION_CHOICES, label="Nivel de Formación", help_text="Seleccione el nivel de formación.")
    modalidad = forms.ChoiceField( choices=Programa.MODALIDAD_CHOICES, label="Modalidad", help_text="Seleccione la modalidad del programa.")
    duracion_meses = forms.CharField(label="Duración en Meses", help_text="Ingrese la duración del programa en meses.")
    duracion_horas = forms.CharField(label="Duración en Horas", help_text="Ingrese la duración del programa en horas.")
    descripcion = forms.CharField(widget=forms.Textarea, label="Descripción del Programa", help_text="Ingrese una descripción del programa.")
    competencias = forms.CharField(widget=forms.Textarea, label="Competencias a Desarrollar",  help_text="Ingrese las competencias que se desarrollarán en el programa.")
    perfil_egreso = forms.CharField(widget=forms.Textarea, label="Perfil de Egreso", help_text="Ingrese el perfil de egreso del programa.")
    requisitos_ingreso = forms.CharField(widget=forms.Textarea, label="Requisitos de Ingreso", help_text="Ingrese los requisitos de ingreso del programa.")
    centro_formacion = forms.CharField(max_length=200, label="Centro de Formación", help_text="Ingrese el centro de formación del programa.")
    regional = forms.CharField(max_length=100, label="Regional", help_text="Ingrese la regional del programa.")
    estado = forms.ChoiceField(choices=Programa.ESTADO_CHOICES, label="Estado", help_text="Seleccione el estado del programa.")
    fecha_creacion = forms.DateField(label="Fecha de Creación del Programa", help_text="Ingrese la fecha de creación del programa.")
    fecha_registro = forms.DateTimeField( label="Fecha de Registro", help_text="Fecha de registro del programa en el sistema.")
    
    def clean(self):
        cleaned_data = super().clean()
        codigo = cleaned_data.get('codigo')
        nombre = cleaned_data.get('nombre')
        
        if not nombre or not codigo:
            raise forms.ValidationError("Todos los campos son obligatorios.")
        
        return cleaned_data
    
    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        if not codigo.isdigit():
            raise forms.ValidationError("El código debe contener solo números.")
        # Validar que el código contenga solo números
        if not codigo.isdigit():
            raise forms.ValidationError("El código debe contener solo números.")
        
        # Validar que el código no exista ya en la base de datos
        if Programa.objects.filter(codigo=codigo).exists():
            raise forms.ValidationError(f"Ya existe un programa con el código '{codigo}'. Por favor, ingrese un código diferente.")
        
        return codigo
    
    def save(self):
        try: 
            programa = Programa.objects.create(
                codigo=self.cleaned_data['codigo'],
                nombre=self.cleaned_data['nombre'],
                nivel_formacion=self.cleaned_data['nivel_formacion'],
                modalidad=self.cleaned_data['modalidad'],
                duracion_meses=self.cleaned_data['duracion_meses'],
                duracion_horas=self.cleaned_data['duracion_horas'],
                descripcion=self.cleaned_data['descripcion'],
                competencias=self.cleaned_data['competencias'],
                perfil_egreso=self.cleaned_data['perfil_egreso'],
                requisitos_ingreso=self.cleaned_data['requisitos_ingreso'],
                centro_formacion=self.cleaned_data['centro_formacion'],
                regional=self.cleaned_data['regional'],
                estado=self.cleaned_data['estado'],
                fecha_creacion=self.cleaned_data['fecha_creacion'],
                fecha_registro=self.cleaned_data['fecha_registro']
            )
            return programa 
        except Exception as e:
            raise forms.ValidationError(f"Error al guardar el programa: {str(e)}")