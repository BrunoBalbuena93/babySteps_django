from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    # Este es para el quickstart
    # path("", include(router.urls)),
    path("", include("snippets.urls")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework"))
]