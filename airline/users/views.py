from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    print("woofwoof")
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid user man"
            })
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged Out manee"
        })
