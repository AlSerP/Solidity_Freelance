from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from django.http import HttpResponse, HttpResponseNotFound
from .forms import New_User, New_Wallet
from .models import Wallet


def index(request):
    return render(request, "mian.html")


def register(request):
    if request.method == 'POST':
        wallet = New_Wallet(request.POST)
        form = New_User(request.POST)
        if form.is_valid() and wallet.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('first_name')
            surname = form.cleaned_data.get('last_name')
            new_wal = wallet.cleaned_data.get('wallet')
            user = User(username=username,password=make_password(password),email=email,first_name=name,last_name=surname)
            user.save()
            new_wallet = Wallet(wallet=new_wal,user_id=user.id)
            new_wallet.save()
            auth.login(request, user)

    else:
        wallet = New_Wallet
        form = New_User

    context = {'form': form, 'wallet': wallet}
    return render(request, 'register.html', context)


