from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

def say_hello(request):
    return render(request,'welcome.html')


def admin(request):
    return render(request,'admin_login.html')

def student(request):
    return render(request,'Student.html')