from sqlite3 import Cursor
from tabnanny import check
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

import mysql.connector as sql

name=''
email=''
pwd=''
type=''



# Create your views here.

def say_hello(request):
    return render(request,'welcome.html')

def add_book(request):
    if request.method == 'POST':
        m=sql.connect(host="localhost",user="root",passwd="new_password",database ="library_management")
        cursor=m.cursor()
        book_name=request.POST['book_name']
        ISBN=request.POST['ISBN']
        author=request.POST['author']
        publication=request.POST['publication']
        c="insert into book_detail( name ,ISBN,author,publication) Values ('{}','{}','{}','{}')".format(book_name,ISBN,author,publication)
        cursor.execute(c)
        m.commit()
        
    return render(request,'add_book.html')

def all_book(request):
    m=sql.connect(host="localhost",user="root",passwd="new_password",database ="library_management")
    cursor=m.cursor()
    c= "select * from book_detail"
    cursor.execute(c)
    t=list(cursor.fetchall())
    print("all book",t)
 
    return render(request,'all_book.html', { 'data': t})

def delete_book(request):
    if request.method == 'POST':
        m=sql.connect(host="localhost",user="root",passwd="new_password",database ="library_management")
        cursor=m.cursor()
        book_id= request.POST['book_id']
        book_name = request.POST['book_name']
        c= "delete from book_detail where book_id ='{}' and name = '{}' ".format(book_id,book_name)
        cursor.execute(c)
        m.commit()

        t = (cursor.fetchone())
        print(t)
        


    return render(request,'delete_book.html')

def update_book(request):
    if request.method == 'POST':
        m=sql.connect(host="localhost",user="root",passwd="new_password",database ="library_management")
        cursor=m.cursor()
        book_id= request.POST['book_id']
        book_name = request.POST['book_name']
        ISBN = request.POST['ISBN']
        author = request.POST['author']
        publication = request.POST['publication']
        c= "update book_detail set name ='{}' , ISBN = '{}',author='{}',publication='{}' where book_id ='{}'  ".format(book_name,ISBN,author,publication,book_id )
        cursor.execute(c)
        m.commit()

        t = (cursor.fetchone())
        print(t)
    return render(request,'update_book.html')


def admin(request):
    if request.method == 'POST':
        m=sql.connect(host="localhost",user="root",passwd="new_password",database ="library_management")
        cursor=m.cursor()
        Email= request.POST['email']
        password = request.POST['password']
        c= "select * from users where email ='{}' and password = '{}' ".format(Email,password)
        cursor.execute(c)
        t = (cursor.fetchone())
        print(t)
        
        print("DONE")
        if t!=():
            if (t[-1] == 'Admin'):
                return render(request,'Admin_portal.html')
            else:
                return student(request)

    # global email,pwd
    # if request.method == 'POST':
    #     m=sql.connect(host="localhost",user="root",passwd="new_password",database ="library_management")
    #     cursor=m.cursor()
    #     d=request.POST
    #     for key,value in d.items():
    #         if key == "email":
    #             email=value
    #         if key == "password1":
    #             pwd=value

    #         i= "select * from users where email='{}' and password='{}'".format(email,pwd)
    #         cursor.execute(i)
    #         t = tuple(cursor.fetchall())
           
     

    return render(request,'admin_login.html')


def student(request):
    m=sql.connect(host="localhost",user="root",passwd="new_password",database ="library_management")
    cursor=m.cursor()
    c= "select * from book_detail"
    cursor.execute(c)
    t=list(cursor.fetchall())
    print("all book",t)
 
    return render(request,'Student_portal.html', { 'data': t})

def admin_register(request):
    global name,email,pwd
    if request.method == 'POST':
        m=sql.connect(host="localhost",user="root",passwd="new_password",database ="library_management")
        cursor=m.cursor()
        type= request.POST['type']
        name = request.POST['fullName']
        email= request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # S=request.POST
        # for key,value in S.items():
        #     if key == "type":
        #         type=value
        #     if key == "fullName":
        #         name=value
        #     if key == "email":
        #         email=value
        #     if key == "password1":
        #         pwd=value
        
        # c="select 1 from users where email = '{}' ".format(email)
        # cursor.execute(c)
        # m.commit()
        # t=cursor.fetchall()
        # print(t)

        if  len(name)<3:
            messages.error(request,"Username must be greater than 3")
        if password1 != password2:
            messages.error(request,"Password do not match")
        # if t!=():
        #     messages.error(request,"Email is already Exist ")

        
        else:

            c= "insert into users Values ('{}','{}','{}','{}')".format(name,email,password2,type)
            try:
                cursor.execute(c)
            except :
                messages.error(request,"Email is already Exist ")


            m.commit()


    return render(request,'admin_register.html')