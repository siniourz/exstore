from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db import IntegrityError


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request,"users/index.html")

def login_view(request):
    if request.method== "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user= authenticate(request, username=username , password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render( request,"users/login.html",{
                "message":"invalid credentials"
            })
    return render(request,"users/login.html")


def logout_view(request):
    logout(request)
    return render(request, "users/index.html",{
        "message":"logged out"
    })

def signup_view(request):
    if request.method== "POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        confirmation=request.POST["confirmation"]

        if password != confirmation:
            return render(request, "users/signup.html",{
                "message":"passwords do not match"
            })
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
        except IntegrityError:
            return render (request, "users/signup.html",{
                "message":"Username aldready taken"
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "users/signup.html")