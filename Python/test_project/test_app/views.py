from django.shortcuts import render
from django.http import HttpResponse
from test_app.models import Users
from test_app.forms import newUser
# Create your views here.

def index(request):
    return render(request, "test_app/index.html", context={"message": "/users"})
    

def users(request):
    users = Users.objects.order_by("name")
    return render(request, "test_app/users.html", context={"users": users})

def help(request):
    textOut = {"help_insert": "This is the help page"}
    return render(request, "test_app/help.html", textOut)

def register(request):
    form = newUser()
    if request.method == "POST":
        form = newUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render(request, "test_app/register.html", context={"form": form})