"""This is a docstring which describes the module"""
import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView
from recipesite.models import User



def login_view(request):
    """This is a docstring which describes the module"""
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "recipesite/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "recipesite/login.html")


def logout_view(request):
    """This is a docstring which describes the module"""
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    """This is a docstring which describes the module"""
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "recipesite/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "recipesite/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "recipesite/register.html")