import datetime
from django.shortcuts import render, redirect
from todolist.models import Task
from django.core import serializers
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from todolist.forms import TaskForm
from django.contrib.auth.models import User

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    username = request.user
    data_barang_wishlist = Task.objects.filter(user=username)
    message = ""
    context = {
        'list_barang': data_barang_wishlist,
        'user': username,
        'message': message,
    }
    return render(request, "todolist.html", context)

def show_xml(request):
    data = Task.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Task.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Task.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Task.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def register(request):
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        password = ""

        user = User.objects.filter(username = username)  
        if password1 and password2 and password1 != password2:
            messages.info(request, "Password berbeda")
            password = None 
        elif user.count():
            messages.info(request, "Akun sudah pernah dibuat")
            username = None 
        else:
            username = username
            password = password2
        
        if username is not None and password is not None:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Akun telah dibuat!')
            return redirect('todolist:login')

    return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title != "" and description != "":
            task = Task(
                title=title,
                description=description,
                user=request.user,
            )
            task.save()
            messages.success(request, "Task berhasil dibuat!")
            return redirect("todolist:show_todolist")

    return render(request, "create-task.html")

@login_required(login_url='/todolist/login/')
def status(request,id):
    status = Task.objects.get(pk=id)
    if status.is_finished:
        status.is_finished = False
    else:
        status.is_finished = True
    status.save()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

@login_required(login_url='/todolist/login/')
def hapus(request,id):
    hapus = Task.objects.get(pk=id)
    hapus.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))
