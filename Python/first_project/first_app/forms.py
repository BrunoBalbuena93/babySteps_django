from django import forms
from django.core import validators
from django.contrib.auth.models import User
from first_app.models import UserProfileInfo

 # Validators
"""
Hay formas para validar un formulario de que la información que está mandando es la correcta o bien,
que es una persona y no un bot quien está llenando el formulario. Hay 3 formas de validar:
Caso 1 Funcion adicional: Cuando generamos una funcion externa que se encarga de checar y se anexa en el argumento del form
Caso 2 Método de la Clase: Agregas un método clean_(nombre del form) y se describe lo que se quiera hacer
Caso 3 Built-In de Django: Django tiene precargados varios métodos de validación que se colocan dentro del argumento
En el ejemplo colocaremos uno de cada uno

También se puede obtener los datos del formulario con el método clean descrito en la clase.
"""


def check_for_capital(value):
    # Vamos a checar que el valor de nombre comience con mayuscula
    if value[0].islower():
        raise forms.ValidationError("Name has to start with Capital letter")
    


class formName(forms.Form):
    topic = forms.CharField()
    url = forms.URLField()
    verify_url = forms.URLField(label="Ingresa de nuevo la URL")
    name = forms.CharField(validators=[check_for_capital])
    text = forms.CharField(widget=forms.Textarea)
    # Los de verificacion para email o contraseña
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    
    
    def clean(self):
        all_clean_data = super().clean()
        url = all_clean_data["url"]
        vurl = all_clean_data["verify_url"]
        if url != vurl:
            raise forms.ValidationError("Las urls no son las mismas")
    
   
    def clean_text(self):
        text = self.cleaned_data["text"]
        # Aqui verificamos que el campo no esté vacio
        if len(text) == 0: 
            raise forms.ValidationError("You have to write something!")
        return text
    
    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ("username", "email", "password")
        

class UserProfileInfoForm(forms.ModelForm):
    # portfolio = forms.URLField(required=False)
    # picture = forms.ImageField(required=False)
    class Meta():
        model = UserProfileInfo
        fields = ("portfolio", "picture")