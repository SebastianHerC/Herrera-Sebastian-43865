from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#___________FORMULARIOS CON DATOS A SOLICITAR_______________
class SedesForm(forms.Form):
    direccion = forms.CharField(label="dirección", max_length= 50, required=True)
    numeracion =forms.IntegerField(label ="numeración", required=True)

class ProfesoresForm(forms.Form):
    nombre = forms.CharField(label="nombre", max_length= 50, required=True)
    clase = forms.CharField(label="clase", max_length= 50, required=True)

class AlumnosForm(forms.Form):
    nombre = forms.CharField(label="nombre", max_length= 50, required=True)
    mail = forms.EmailField(label="email", required=True)
    edad= forms.IntegerField(label="edad", required=True)

class ClasesForm(forms.Form):
    nombre = forms.CharField(label="nombre", max_length= 50, required=True)
    dia = forms.CharField(label="día", max_length= 50, required=True)
    hora = forms.CharField(label="hora", max_length= 50, required=True)
    valor = forms.IntegerField(label="valor", required=True)

class RegistroUsuariosForm(UserCreationForm):
    email=forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label='Contraseña', widget =forms.PasswordInput)
    password2=forms.CharField(label='Confirmar Contraseña', widget =forms.PasswordInput)
    
    class Meta:    
        model= User 
        fields=['username', 'email', 'password1','password2']
        help_text ={k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)

    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email', 'password1', 'password2' ] 
        help_texts = { k:"" for k in fields}


class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)

