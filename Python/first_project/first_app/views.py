from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# importando las tablas (modelos)
from first_app.models import Topic, AccessRecord, Webpage
from .forms import formName, UserForm, UserProfileInfoForm
# Para el login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    # Generamos una query de AccessRecords ordenados por date
    context = {"text": "Hello mate", "number": 40}
    return render(request, "first_app/index.html", context=context)


def other(request):
    return render(request, "first_app/other.html")


def relative(request):
    return render(request, "first_app/relative_url_template.html")
    
    
def forms(request):
    form = formName()
    # Verificamos que el servicio sea POST
    if request.method == "POST":
        form = formName(request.POST)
        # Verificamos que sea válido
        if form.is_valid():
            # Hacer algo con lo que llegó
            print("Validación completada")
            print("Topic : " + form.cleaned_data["topic"])
            print("Name: " + form.cleaned_data["name"])
            
    return render(request, "first_app/formsPage.html", context={"form": form})


def register(request):
    isRegistered = False
    # Primero verificamos si se está mandando data con el formulario
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        # Verificamos que los datos sean válidos
        if user_form.is_valid() and profile_form.is_valid():
            # Primero hasheamos la contraseña
            user = user_form.save()
            user.set_password(user.password)
            user.save()                
            
            profile = profile_form.save(commit=False)
            profile.user = user
            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]
            profile.save()
            isRegistered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, "first_app/register.html", {"user_form": user_form, "profile_form": profile_form, "registered": isRegistered })
            
            
def user_login(request):
    print("help!")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                # Ya que entró, lo mandamos al inicio
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("Cuenta no activa")
        else:
            print("LogIn fallido.\nusername: {}\npassword: {}".format(username, password))
            return HttpResponse("Usuario inválido")
    else:
        return render(request, "first_app/login.html")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))