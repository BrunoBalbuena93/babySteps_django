from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    class Meta():
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()
    
    def __init__(self, *args, **kwags):
        super().__init__(*args, **kwags)
        # Esto es para poner el placeholder customizado
        self.fields["username"].label = "Nombre de usuario"
        self.fields["email"].label = "Tu email"
        self.fields["password1"].label = "Tu contraseña"
        self.fields["password2"].label = "Confirma tu contraseña"