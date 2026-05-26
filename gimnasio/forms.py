from django import forms
from .models import Socio, Membresia


class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['nombre', 'email', 'membresia', 'activo', 'foto']


class MembresiaForm(forms.ModelForm):
    class Meta:
        model = Membresia
        fields = ['tipo', 'precio', 'duracion_meses', 'beneficios']
        widgets = {
            'beneficios': forms.Textarea(attrs={'rows': 4}),
        }
