from rest_framework import serializers as sr 
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
"""
Un serializer es un medio para parsear información de un formato a otro y viceversa, por ejemplo podemos convertir una query en un json.
Para esto hay dos formas de hacerlo, similar a los modelos Form y ModelForm de Django, existe Serializer y ModelSerializer.
Serializer: Se construye a la "par" del modelo y se definen las funciones de crear, actualizar y borrar
ModelSerializer: Se agrega el modelo en la clase Meta, se denotan los campos y listo.

Hiperlink. En este ejemplo se hara hipervinculo por entidades, para ello cambiaremos el ModelSerializer por un HyperlinkedModelSerializer.
Existen diferencias con ello:
- No incluye el campo de id por default
- Incluye un campo url como HyperlinkedIdentityField
- Las relaciones usan esos campos url en lugar de las primary keys
"""

# HyperlinkedModelUser
class UserSerializer(sr.HyperlinkedModelSerializer):
    snippets = sr.HyperlinkedRelatedField(many=True, view_name="snippet-detail", read_only=True)
    
    class Meta:
        model = User
        fields = ["url", "id", "username", "snippets"]



# HyperlinkedModel
class SnippetSerializer(sr.HyperlinkedModelSerializer):
    owner = sr.ReadOnlyField(source='owner.username')
    highlight = sr.HyperlinkedIdentityField(view_name="snippet-highlight", format="html")
    
    class Meta:
        model = Snippet
        fields = ["url", "id", "highlight", "owner", "title", "code", "linenos", "language", "style"]


# ModelUser
class ModelUserSerializer(sr.ModelSerializer):
    snippets = sr.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    
    class Meta:
        model = User
        fields = ["id", "username", "snippets"]

# ModelSerializer
class ModelSnippetSerializer(sr.ModelSerializer):
    # Análogo a decir CharField(read_only=True)
    owner = sr.ReadOnlyField(source="owner.username")
    class Meta:
        model = Snippet
        fields = ["id", "owner", "title", "code", "linenos", "language", "style"]


# Serializer
class RawSnippetSerializer(sr.Serializer):
    """
    Este serializer va en correspondencia con el snippet hecho en models, tiene los mismos campos y especificamos en caso de ser requeridos
    """
    # ID a manera de PK
    id = sr.IntegerField(read_only=True)
    # Titulo que no es estrictamente necesario
    title = sr.CharField(required=False, allow_blank=True, max_length=100)
    # code
    code = sr.CharField(style={'base_template': 'textarea.html'})
    # linenos No necesario
    linenos = sr.BooleanField(required=False)
    #
    language = sr.ChoiceField(choices=LANGUAGE_CHOICES, default="python")
    # Style
    style = sr.ChoiceField(choices=STYLE_CHOICES, default="friendly")
    
    
    def create(self, validated_data):
        "Crea y regresa una instancia de Snippet para data ya validada"
        return Snippet.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        "Tal cual, es un update de data validada"
        instance.title = validated_data.get("title", instance.title)
        instance.code = validated_data.get("code", instance.code)
        instance.linenos = validated_data.get("linenos", instance.linenos)
        instance.language = validated_data.get("language", instance.language)
        instance.style = validated_data.get("style", instance.style)
        instance.save()
        return instance
    
    