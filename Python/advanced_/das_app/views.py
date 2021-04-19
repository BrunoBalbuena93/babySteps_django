from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView
# Los que se realizan funciones ejecutivas en los modelos
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from das_app import models

# Reemplazaremos esto con un Class Based View
# def index(request):
    # return render(request, "index.html")

# Esta clase es para retornar views pero no necesariamente para templates
# class CBView(View):
#     def get(self, request):
#         return HttpResponse("Class Based Views index")

# Esta clase si trae los templates
class IndexView(TemplateView):
    template_name = "index.html"
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["inject_me"] = "BASIC INJECTION"
    #     return context
    

class SchoolList(ListView):
    # Seleccionamos el nombre que tendrá la variable en lista con context_object_name
    context_object_name = "schools"
    model = models.School
    

class SchoolDetail(DetailView):
    # Seleccionamos el nombre que tendrá la variable en lista con context_object_name
    context_object_name = "school_detail"
    model = models.School
    template_name = 'das_app/School_detail.html'
    

class SchoolCreateView(CreateView):
    # Primero diremos que campos podrá llenar
    fields = ("name", "principal", "location")
    model = models.School
    
    
class SchoolUpdateView(UpdateView):
    # Debes definir que campos se pueden actualizar
    fields = ("name", "principal")
    model = models.School
    
class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("das_app:list")