from django.db import models
from django.db.models.base import Model
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


class Persona(models.Model):
    nombre = models.CharField(max_length=10)
    email = models.EmailField(unique=True)