from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('', views.say_hello),
    path('admin_login/', views.admin),
    path('student/', views.student),
    path('admin_register/', views.admin_register),
]
