from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer

from rest_framework import status
from rest_framework.decorators import api_view, APIView, action
from rest_framework.response import Response
# MIXINS
from rest_framework import mixins as mx
from rest_framework import generics as gen
# AUTH
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
# ENDPOINTS Y HYPERLINKING
from rest_framework.reverse import reverse
from rest_framework import renderers as rest_renderer
# VIEWSETS
from rest_framework import viewsets
"""
En este script se abordan las views con 3 formas distintas:
- ViewSets: 
Las ViewSets son similares a las ViewClasses, slo que se les dan las operaciones de lectura y actualización (read & update) en lugar
de los metodos convencionales get y put. Una VewSet esta limitada a un set de metodos, permite que el developer solo trabaje con 
los modelos de interacción y deja que la clase se encargue directamente de los direcionamientos URL (Hipervinculación por url y no por primary keys)
Clases: 

- ClassBased Views:
Similar a las ViewClass normales de django, estas tienen templates básicos que sirven para las operaciones de GET, POST, PUT y DELETE.
En este script tenemos 3 tipos de clases.
Clases con APIView: Donde definimos get, put y delete 
[SnippetList, SnippetDetail, UserList, UserDetail]
Clases con Mixins: Donde no configuramos como tal los métodos, sino que utilizamos mixins para complementar el código. Tal es el caso
                   al definir "get" simplemente se hace un return retrieve(), parte de la herencia del Mixin 
[MixinSnippetList, MixinSnippetDetail]
Clases Built-in: Estas clases estan implementadas con dichos mixins. 
[BuiltSnippetList, BuiltSnippetDetail]

- Function Views:
En estas funciones es tal cual paso a paso denotar lo que se pretende hacer, i.e., paso a paso configurar cada opción.
En el caso de las funciones, se agrega el decorador api_view denotando los métodos que se implementerán.
[snippet_list, snippet_detail, api_root]


(1) perform_create: Se hace un override de perform_create dado que se debe almacenar también el usuario, el cual no va dentro del body enviado sino en el header
(2) action: Corresponde a que estamos creando una accion custom que no cae en los comandos "create", "delete" ni "update". Las acciones configuradas responden
            como "GET" por default, para cambiarlo se usa el argumento methods="POST". En caso de querer que el nombre de api sea distinto al nombre del método
            se debe especificar el argumento url_path en action.
"""

# Usuarios: Cambiamos 2 Views por un ViewSet
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    # Esta viewset genera "list" y "details" de manera automática
    # Configurando el queryset
    queryset = User.objects.all()
    # Configurando el traductor
    serializer_class = UserSerializer


# Snippets: Reemplazamos 3 clases con una ViewSet
class SnippetViewSet(viewsets.ModelViewSet):
    # Automaticamente genera List, Create, Retrieve, Update y Destroy
    # Configurando el queryset
    queryset = Snippet.objects.all()
    # Configurando el traductor
    serializer_class = SnippetSerializer
    # Agregando los permisos para poder editar
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    # Creamos el metodo para highlight (2)
    @action(detail=True, renderer_classes=[rest_renderer.StaticHTMLRenderer])
    def highlight(self, request, *ags, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    # Override (1)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user) 


# Renderer de snippets/<pk>/highlight/ Solo es vista
class SnippetHighlight(gen.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [rest_renderer.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

# Root de extensiones. Se colocan hipervinculos para navegar entre los endpoints
@api_view(["GET"])
def api_root(request, format=None):
    # Direcciones a donde se puede enviar
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse("snippet-list", request=request, format=format)
    })



# Lista de usuarios
class UserList(gen.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(gen.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Clases all built-in

class BuiltSnippetList(gen.ListCreateAPIView):
    # Definiendo el queryset a trabajar
    queryset = Snippet.objects.all()
    # Definiendo el traductor
    serializer_class = SnippetSerializer
    # Agregando permisos
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    # Override (1)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

class BuiltSnippetDetail(gen.RetrieveUpdateDestroyAPIView):
    # Definiendo el queryset a trabajar
    queryset = Snippet.objects.all()
    # Definiendo el traductor
    serializer_class = SnippetSerializer
    # Agregando permisos
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    

# Clases con mixins

class MixinSnippetList(mx.ListModelMixin, mx.CreateModelMixin, gen.GenericAPIView):
    # Definiendo el queryset a trabajar
    queryset = Snippet.objects.all()
    # Definiendo el traductor
    serializer_class = SnippetSerializer

    # Definiendo get
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    # Definiendo post
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    # Override (1)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

class MixinSnippetDetail(mx.RetrieveModelMixin, mx.UpdateModelMixin, mx.DestroyModelMixin, gen.GenericAPIView):
    # Definiendo queryset
    queryset = Snippet.objects.all()
    # Definiendo el traductor
    serializer_class = SnippetSerializer
    
    # Definiendo get
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    

    # Definiendo update
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    # Definiendo delete
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
    
    
# Clases
class SnippetList(APIView):
    """
    Como una ListView, lista de snippets o crea uno nuevo
    """
    def get(self, request, format=None):
        # Primero instanciamos todas las entradas de snippets (paso prescindible)
        snippets = Snippet.objects.all() 
        # Se crea el serializador para traducirlo a json response
        serializer = SnippetSerializer(snippets, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        # Si el proceso se realizó con exito, guarda el snippet y retorna la información y status OK
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # De lo contrario, retorna el error con status 400
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)        
        
class SnippetDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
    
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
# Funciones
@api_view(["GET", "POST"])
def snippet_list(request, format=None):
    """
    Aqui tendremos dos métodos, cuando es GET te enlista los snippets existentes, con POST, crea uno nuevo
    """
    if request.method == "GET":
        # Primero instanciamos todas las entradas de snippets (paso prescindible)
        snippets = Snippet.objects.all() 
        # Se crea el serializador para traducirlo a json response
        serializer = SnippetSerializer(snippets, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    
    elif request.method == "POST":
        # Se parsea la información a Json
        # data = JSONParser().parse(request)
        # La info a manera de json se convierte al modelo de snippet
        serializer = SnippetSerializer(data=request.data)
        # Si el proceso se realizó con exito, guarda el snippet y retorna la información y status OK
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # De lo contrario, retorna el error con status 400
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET", "PUT", "DELETE"])
def snippet_detail(request, pk, format=None):
    try:
        # Primero obtenemos el snippet solicitado
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Solicitar el snippet
    if request.method == "GET":
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    
    # Update del snippet
    elif request.method == "PUT":
        # Parsea la información para el update / se quita si se trabaja con api_view
        # data = JSONParser().parse(request)
        # Checa los campos que se deban de modificar
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    