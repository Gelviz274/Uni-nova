from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username', 'required': True}))
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'required': True}))

class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username', 'required': True}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'email@example.com', 'required': True}))
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'required': True}))
    confirm_password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'placeholder': 'Verificar Contraseña', 'required': True}))

