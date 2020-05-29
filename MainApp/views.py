from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseNotFound
from .forms import New_User, New_Wallet
from .models import Wallet, Task
from django.http import Http404


def index(request):
    return render(request, "main.html")


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        name = request.POST.get('first_name')
        surname = request.POST.get('last_name')
        new_wal = request.POST.get('wallet')
        print(username, password, email, name, surname, new_wal)
        user = User(username=username, password=make_password(password), email=email, first_name=name,
                    last_name=surname)
        user.save()
        # TODO: закоменченная херня снизу не работает
        wallet = Wallet(wallet=new_wal, user_id=user.id)
        wallet.save()
        auth.login(request, user)

    return render(request, 'register.html')
    # return redirect("/")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password, "try to log in")
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)

        else:
            print("Auth problems ...")
        return redirect("/")

    else:
        print("HUGE PROBLEM")
        raise Http404

    print(username, "logged in")
    return redirect('/')


def logout_page(request):
    logout(request)
    return redirect('/')


def user_info(request):
    user_info = request.user
    # info = UserInfo.objects.get(userid=user_info.pk)
    # return render(request, 'user_info.html', {"info": info, "user_info": user_info})
    return render(request, 'user_info.html', {"user_info": user_info})


@login_required()
def user_status(request):
    u = request.user.pk
    info = User.objects.get(id=u)
    wallet = Wallet.objects.get(user_id=u)
    context = {'info': info, 'wallet': wallet}
    return render(request, "info.html", context)


def create_task(request):
    if request.method == 'POST':
        name = request.get('name')
        description = request.get('describe')
        cost = request.get('cost')
        u = request.user
        task = Task(user=u, cost=cost, name=name, describe=description)


def all_tasks(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, "tasks.html", context)
