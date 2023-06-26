from django.contrib import admin


from django.contrib.auth.models import User 
from . models import Contact, ContactAdmin 

# Register your models here.

admin.site.register(Contact,ContactAdmin)











