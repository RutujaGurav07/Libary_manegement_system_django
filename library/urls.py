from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('welcome/', views.say_hello),
    path('welcome/', views.is_logged),
    path('login/', views.login),
    path('Student_portal/', views.student),
    path('admin_register/', views.admin_register),
    path('Admin_portal/', views.admin_portal),
    path('add_book/', views.add_book),
    path('all_book/', views.all_book),
    path('delete_book/', views.delete_book),
    path('update_book/', views.update_book),
    # path('update_book/', views.update_book),

]
