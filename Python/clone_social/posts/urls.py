from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    # Todos los posts
    path("", views.PostList.as_view(), name="all"),
    # Nuevo Post
    path("new/", views.CreatePost.as_view(), name="create"),
    # Post del usuario X
    path("by/<username>/", views.UserPosts.as_view(), name="for_user"),
    # Ver un post específico
    path("by/<username>/<pk>/", views.PostDetail.as_view(), name="single"),
    # Borrar post determinado
    path("delete/<pk>/", views.DeletePost.as_view(), name="delete"),
]