from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from Usuarios.models import UserN

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        # Agregar clases de Bootstrap a los campos del formulario
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Username', 'required': True})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Contraseña', 'required': True})

class RegistroForm(UserCreationForm):
    class Meta:
        model = UserN
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        # Agregar clases de Bootstrap a los campos del formulario
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Username', 'required': True})
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'email@example.com', 'required': True})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Contraseña', 'required': True})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Verificar Contraseña', 'required': True})