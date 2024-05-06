from django.shortcuts import render, redirect

# librería para el formulario de registro
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# librería para registrar al usuario en la DB
from django.contrib.auth.models import User

# librería para cookie de login y logout
from django.contrib.auth import login, logout, authenticate

from django.db import IntegrityError


# Create your views here.
def home(request):
    return render(request, "home.html")


def signup(request):

    if request.method == "GET":
        return render(request, "signup.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            # registrar usuario
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect("wiki")
            except IntegrityError:
                return render(
                    request,
                    "signup.html",
                    {"form": UserCreationForm, "error": "Usuario ya existe"},
                )
        else:
            return render(
                request,
                "signup.html",
                {"form": UserCreationForm, "error": "Constraseñas no coinciden"},
            )


def wiki(request):
    return render(request, "wiki.html")


def signout(request):
    logout(request)
    return redirect("home")


def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "signin.html",
                {
                    "form": AuthenticationForm,
                    "error": "nombre de usuario o contraseña incorrectos",
                },
            )
        else:
            login(request, user)
            return redirect("wiki")
