from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializer import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    "API endpoint para ver y editar usuarios"
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class GroupViewSet(viewsets.ModelViewSet):
    "API endpoint para ver grupos"
    queryset = Group.objects.all().order_by("-date_joined")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
