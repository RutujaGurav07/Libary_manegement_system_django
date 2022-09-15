from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.

def say_hello(request):
    return render(request,'welcome.html')


def admin(request):
    return render(request,'admin_login.html')

def student(request):
    return render(request,'Student.html')

def admin_register(request):
    if request.method == 'POST':
        name = request.POST['fullName']
        email= request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.query.filter_by(email=email).first()
        if user:
            messages.info(request,'Email Already Exists!',category='error')
        elif len(email) < 4:
            messages.info(request,'Email must be greater than 3 characters.', category='error')
        elif len(name) < 3:
            messages.info(request,'Full Name must be greater than 2 characters.', category='error')
        elif password1 != password2:
            messages.info(request,'Passwords Don\'t Match.', category='error')
        elif len(password1) < 8:
            messages.info(request,'Password must be at least 8 characters.', category='error')
        else:
            user = User.objects.create_user(name=name, password=password2, email=email )
            user.save()
            messages.info(request,'User Created ')
        return redirect('/')

    return render(request,'admin_register.html')