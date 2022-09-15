import email
from pyexpat import model
from django.db import models

# Create your models here.
class Admin_Data (models.Model):
    name = models.CharField(max_length=100,null=False)
    email= models.EmailField(max_length=50,null=False,unique=True)
    password= models.CharField(max_length=20,null=False)