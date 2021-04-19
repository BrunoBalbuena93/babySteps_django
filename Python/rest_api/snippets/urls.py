from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import renderers
# ROUTERS
from rest_framework.routers import DefaultRouter

"""
En esta sección se abordan las distintas configuraciones de conexión.

Que es "hiperlinkear" la API? 
Crear relaciones entre las entidades de la API, para ello hay varias formas de relacionarlas
 + Por Primary Keys
 + Usando hipervinculos entre las entidades
 + Usando slugs
 + Usando la representación en string
 + Anidando las relaciones en forma de padres
 
 Routers
 Los routers solo se usan con ViewSets, donde se coloca el prefijo (el tipo de url por así decirlo)
 y el viewset. En caso de que el ViewSet no tenga un Queryset, se tiene que colocar un basename. Un ejemplo:
 
 router.register(r'users', UserViewSet)
 -->
 URL:
 Path   ----> Name
 users/ ----> user-list
users/pk/---> user-detail
"""
# Modo: {1: funciones, 2: clases, 3: clases + mixins, 4: clases built-in, 5: ViewSets con path 6: Routers}
modo = 6

if modo == 1:
    # Unicamente funciones
    urlpatterns = format_suffix_patterns([
        # Root
    path("", views.api_root, name="root"),
    # Para ver todos o agregar uno
    path("snippets/", views.snippet_list),
    # Para detalles
    path("snippets/<int:pk>/", views.snippet_detail),
    ])
    
elif modo == 2:
    # Clases sencillas
    urlpatterns = format_suffix_patterns([
        # Root
        path("", views.api_root, name="root"),
        # Para ver todos o agregar uno
        path("snippets/", views.SnippetList.as_view()),
        # Para detalles
        path("snippets/<int:pk>/", views.SnippetDetail.as_view()),
        # Highlight
        path("snippets/<int:pk>/highlight/", views.SnippetHighlight.as_view(), name="snippet-highlight"),   
        # Lista de usuarios
        path("users/", views.UserList.as_view(), name="user-list"),
        # Detalles de usuario
        path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    ])

elif modo == 3:
    # Clases + mixins
    urlpatterns = format_suffix_patterns([
        # Root
        path("", views.api_root, name="root"),
        # Para ver todos o agregar uno
        path("snippets/", views.MixinSnippetList.as_view()),
        # Para detalles
        path("snippets/<int:pk>/", views.MixinSnippetDetail.as_view()),
        # Highlight
        path("snippets/<int:pk>/highlight/", views.SnippetHighlight.as_view(), name="snippet-highlight"), 
        # Lista de usuarios
        path("users/", views.UserList.as_view(), name="user-list"),
        # Detalles de usuario
        path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    ])

elif modo == 4:
    # Clases built-in
    urlpatterns = format_suffix_patterns([
        # Root
        path("", views.api_root, name="root"),
        # Para ver todos o agregar uno
        path("snippets/", views.BuiltSnippetList.as_view(), name="snippet-list"),
        # Para detalles
        path("snippets/<int:pk>/", views.BuiltSnippetDetail.as_view(), name="snippet-detail"),
        # Highlight
        path("snippets/<int:pk>/highlight/", views.SnippetHighlight.as_view(), name="snippet-highlight"), 
        # Lista de usuarios
        path("users/", views.UserList.as_view(), name="user-list"),
        # Detalles de usuario
        path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    ])
    
elif modo == 5:
    # ViewSets en path
    # Primero se configuran las viewSets como views
    # View snippets/
    snippet_list = views.SnippetViewSet.as_view({'get': 'list', 'post':'create'})
    # View snippets/pk/
    snippet_detail = views.SnippetViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
    # View snippets/pk/highlight | Como este metodo es agregado le ponemos el renderer 
    snippet_highlight = views.SnippetViewSet.as_view({'get': 'highlight'}, renderer_classes=[renderers.StaticHTMLRenderer])
    # View users/
    user_list = views.UserViewSet.as_view({ 'get': 'list' })
    # View users/pk/
    user_detail = views.UserViewSet.as_view({'get': 'retrieve'})
    # Ahora configuramos los patterns
    urlpatterns = format_suffix_patterns([
        path("", views.api_root),
        path("snippets/", snippet_list, name="snippet-list"),
        path("snippets/<int:pk>/", snippet_detail, name="snippet-detail"),
        path("snippets/<int:pk>/highlight/", snippet_highlight, name="snippet-highlight"),
        path("users/", user_list, name="user-list"),
        path("users/<int:pk>/", user_detail, name="user-detail"),
        
    ])
    
elif modo == 6:
    # Routers
    router = DefaultRouter()
    # El DefaultRouter crea un root 
    router.register(r'snippets', views.SnippetViewSet)
    router.register(r'user', views.UserViewSet)
    urlpatterns = [
        path("", include(router.urls))
    ]
    
else:
    raise ValueError("No se asigno un valor de modo, hay que seleccionar entre 1 y 6")    