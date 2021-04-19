from django.conf.urls import url
from django.urls import path
from first_app import views

# Para template tagging
app_name = "first_app"

urlpatterns = [
    path("forms/", views.forms, name="forms"),
    path("other/", views.other, name="other"),
    path("relative/", views.relative, name="relative"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    # url(r'^$', views.index, name="index"),
]