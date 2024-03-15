from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Grade,Material
from django.views.generic import ListView, DetailView

# Create your views here.


def home(request):
    if not request.user.is_authenticated:
        return redirect('login-page')
    return render(request,'notebook/homepage.html')


def Materials(request):
    if request.user.is_authenticated:
        return redirect('login-page')
    materials = Material.objects.all()
    return render(request,'notebook/materials.html',{'materials':materials})

def Grades(request):
    if request.user.is_authenticated:
        return redirect('login-page')
    grades = Grade.objects.all()
    

    return render(request,'notebook/grades.html',{'grades' : grades})
