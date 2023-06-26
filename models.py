from pickle import FALSE
from django.conf import settings

from django.db import models

from django.contrib import admin 


# Create your models here.


class Contact(models.Model):
      name = models.CharField(max_length=255)    
      email = models.EmailField(max_length=100)
      message = models.TextField(max_length=255)
      date = models.DateTimeField(auto_now=True)
      
class ContactAdmin(admin.ModelAdmin):    
      list_display  =('email','name','message','date')










