from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # Home
    path("", views.PostList.as_view(), name="post_list"),
    # Post detail
    path("post/<int:pk>/", views.PostDetail.as_view(), name="post_detail"),
    # Pagina about
    path('about/', views.About.as_view(), name="about"),
    # New post
    path("post/new/", views.CreatePost.as_view(), name="post_new"),
    # Edit post
    path("post/<int:pk>/edit/", views.PostUpdate.as_view(), name="post_edit"),
    # Delete post
    path("post/<int:pk>/delete/", views.PostDelete.as_view(), name="post_remove"),
    # Drafts
    path("drafts/", views.Draft.as_view(), name="drafts"),
    # Publicar post
    path("post/<int:pk>/publish/", views.post_publish, name="post_publish"),
    # Añadir comentario
    path("post/<int:pk>/comment/", views.add_comment_to_post, name="add_comment_to_post"),
    # Aprobar un comentario
    path("comment/<int:pk>/approve/", views.comment_approve, name="comment_approve"),
    # Borrar un comentario
    path("comment/<int:pk>/remove/", views.comment_remove, name="comment_remove"),
]
