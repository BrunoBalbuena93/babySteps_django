from django.conf.urls import url
from django.urls import path
from test_app import views

urlpatterns = [
    path('users/', views.users, name="users"),
    path("register/", views.register, name="register"),
    url(r'^help', views.help, name="help"),
]