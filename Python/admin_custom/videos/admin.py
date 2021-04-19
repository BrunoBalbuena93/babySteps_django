from django.contrib import admin
from .models import Customer, Movie


class MovieAdmin(admin.ModelAdmin):
    # Orden en el que se quiera tener el detailview
    fields = ["release_year", "title", "length"]
    # Para buscar
    search_fields = ["title"]
    # Para hacer filtros
    list_filter = ["release_year", "title"]
    # Forma en la que se muestra la lista de items
    list_display = ["title", "release_year", "length"]
    # 
    list_editable = ["length"]


admin.site.register(Customer)
# Se agrega junto con el modelo
admin.site.register(Movie, MovieAdmin)

