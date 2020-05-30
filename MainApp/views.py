from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseNotFound
from .forms import New_User, New_Wallet
import datetime
from .models import Wallet, Task
from django.http import Http404


def index(request):
    """Main page with all tasks"""
    tasks = Task.objects.all()
    return render(request, "main.html", {"tasks": tasks})


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
        wallet = Wallet(wallet=new_wal, user_id=user.id)
        wallet.save()
        auth.login(request, user)

        return redirect("/")

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


def user_info(request, u_id):
    """Get user's info by his id"""
    for user in User.objects.all():
        print(user.id)
    print('Hi')
    u_info = User.objects.get(id=u_id)
    # info = UserInfo.objects.get(userid=user_info.pk)
    # return render(request, 'user_info.html', {"info": info, "user_info": user_info})
    return render(request, 'user_info.html', {"user_info": u_info})


def task_info(request, t_id):
    t_info = Task.objects.get(id=t_id)
    return render(request, 'task_info.html', {"task_info": t_info})


@login_required()
def user_status(request):
    """Unused"""
    u = request.user.pk
    info = User.objects.get(id=u)
    wallet = Wallet.objects.get(user_id=u)
    context = {'info': info, 'wallet': wallet}
    return render(request, "info.html", context)


def task(request):
    """Render page of new task creations"""
    return render(request, "new_task.html")


def create_task(request):
    """Creates a new task in D  B"""
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        reward = request.POST.get("cost")
        date = datetime.datetime.now()
        user = request.user

        print(title, description, reward, user.username, "Creating task")
        task2 = Task(title=title, description=description, cost=reward, date=date, user=user)
        task2.save()
        print("Task is created")
        return redirect('/')
    else:
        print("HUGE PROBLEM")
        raise Http404

