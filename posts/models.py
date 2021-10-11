from django.db import models
from django.db.models.fields import EmailField

class Users(models.Model):
    emali = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True , null= True)
    created = models.DateTimeField(auto_now_add= True)
    modifa = models.DateTimeField(auto_now= True)




class Tabla_pueba(models.Model):
    campo1 = models.CharField(max_length=200)