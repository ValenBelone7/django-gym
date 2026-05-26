from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class UsuarioRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', 'telefono', 'fecha_nacimiento', 'direccion']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email ya está registrado')
        return email
