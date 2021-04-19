from django import forms
from django.core import validators
from test_app.models import Users

"""
Aqui vamos a conectar el formulario con el modelo de sqlite
"""

class newUser(forms.ModelForm):
    class Meta():
        # Cada modelo debe estar declarado independientemente
        model = Users
        fields = "__all__"
        
    
    