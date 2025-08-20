from django import forms
from .models import Aprendiz, Curso
from apoyos.models import Apoyos

class AprendizForm(forms.Form):
    documento_identidad = forms.CharField(max_length=20, label="Documento de Identidad")
    nombre = forms.CharField(max_length=100, label="Nombre")
    apellido = forms.CharField(max_length=100, label="Apellido")
    telefono = forms.CharField(max_length=10, label="Teléfono")
    correo = forms.EmailField(label="Correo Electrónico")
    fecha_nacimiento = forms.DateField(label="Fecha de Nacimiento")
    ciudad = forms.CharField(max_length=100, required=False, label="Ciudad")
    programa = forms.CharField(max_length=100, required=False, label="Programa de Formación")
    apoyos = forms.ChoiceField(
        choices=Aprendiz.APOYOS_CHOICES, 
        label="Apoyo SENA", 
        help_text="Seleccione el apoyo al cual pertenece.",
        required=False
    )
    monto_apoyo = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        label="Monto del Apoyo",
        help_text="Ingrese el monto si aplica"
    )
    observaciones_apoyo = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False,
        label="Observaciones del Apoyo"
    )
    
    def clean(self):
        cleaned_data = super().clean()
        documento = cleaned_data.get('documento_identidad')
        nombre = cleaned_data.get('nombre')
        apellido = cleaned_data.get('apellido')

        if not documento or not nombre or not apellido:
            raise forms.ValidationError("Todos los campos son obligatorios.")

        return cleaned_data
    
    def clean_documento_identidad(self):
        documento = self.cleaned_data['documento_identidad']
        if not documento.isdigit():
            raise forms.ValidationError("El documento debe contener solo números.")
        
        if Aprendiz.objects.filter(documento_identidad=documento).exists():
            raise forms.ValidationError("Ya existe un aprendiz con este documento de identidad.")
        
        return documento

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono and not telefono.isdigit():
            raise forms.ValidationError("El teléfono debe contener solo números.")
        return telefono
    
    def clean_monto_apoyo(self):
        monto = self.cleaned_data.get('monto_apoyo')
        apoyo_tipo = self.cleaned_data.get('apoyos')
        
        if apoyo_tipo and apoyo_tipo != 'NA' and monto and monto <= 0:
            raise forms.ValidationError("El monto debe ser mayor a 0.")
        
        return monto
    
    def save(self):
        aprendiz = Aprendiz.objects.create(
            documento_identidad=self.cleaned_data['documento_identidad'],
            nombre=self.cleaned_data['nombre'],
            apellido=self.cleaned_data['apellido'],
            telefono=self.cleaned_data.get('telefono'),
            correo=self.cleaned_data.get('correo'),
            fecha_nacimiento=self.cleaned_data['fecha_nacimiento'],
            ciudad=self.cleaned_data.get('ciudad'),
            programa=self.cleaned_data.get('programa', 'No especificado'),
            apoyos=self.cleaned_data.get('apoyos', 'NA')
        )
        
        tipo_apoyo = self.cleaned_data.get('apoyos')
        if tipo_apoyo and tipo_apoyo != 'NA':
            Apoyos.objects.create(
                aprendiz=aprendiz,
                tipo_apoyo=tipo_apoyo,
                monto=self.cleaned_data.get('monto_apoyo'),
                observaciones=self.cleaned_data.get('observaciones_apoyo')
            )
        
        return aprendiz