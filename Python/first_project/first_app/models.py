from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    # Creando una relacion 1 a 1 para poder agregar datos aparte de los precargados
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    
    # Agregando campos extras
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to="profile_pics", blank=True)

    def __str__(self):
        return self.user.username


# Las clases de models van a representar tablas.
# Creando la tabla Topic: 
class Topic(models.Model):
    # top_name representa uno de las columnas de la tabla
    top_name = models.CharField(max_length=264, unique=True)
    
    # Representación de la tabla
    def __str__(self):
        return self.top_name

# Tabla webpages
class Webpage(models.Model):
    # Aqui tenemos una foreign Key de la tabla topic
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    # Nombre de la pagina
    name = models.CharField(max_length=264, unique=True)
    # URL de la pagina
    url = models.URLField(unique=True)
    
    def __str__(self):
        return self.name
    
class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.PROTECT)
    date = models.DateField()
    
    def __str__(self):
        return str(self.date)