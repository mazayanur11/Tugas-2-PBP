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

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    username = request.user
    data_barang_wishlist = Task.objects.filter(user=username)
    context = {
        'list_barang': data_barang_wishlist,
        'user': username,
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
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

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

@login_required(login_url='login/')
def create_task(request):
    form = TaskForm(request.POST)
    if request.method == 'POST':
        form.instance.user = request.user
        if form.is_valid():
            form.save()
        return redirect('todolist:show_todolist')
    context = {'form':form}
    return render(request, "create-task.html", context)

def status(request,id):
    status = Task.objects.get(pk=id)
    if status.is_finished:
        status.is_finished = False
    else:
        status.is_finished = True
    status.save()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

def hapus(request,id):
    hapus = Task.objects.get(pk=id)
    hapus.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))
