from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permision(self, request, view, obj):
        # Permisos de lectura se aplican para cualquier request, por lo que si request.method == GET, pasa
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Concede el permiso si el dueño del objeto es el mismo que el usuario que hace request
        return obj.owner == request.user
    