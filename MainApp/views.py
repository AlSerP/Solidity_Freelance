from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello pediki')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        user = User(username=username, password=make_password(password), first_name=name, last_name=surname,
                    email=email)
        user.save()
        auth.login(request,user)

