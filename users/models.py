from django.db import models
from django.db import models
from django.db.models.base import ModelState
from django.db.models.deletion import CASCADE, RestrictedError
# Create your models here.
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    website = models.URLField(max_length=200,blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20,blank=True)

    pcture = models.ImageField(upload_to='user/pictures',
    blank = True,
    null = True
    )

    created = models.DateTimeField(auto_now_add=True)
    modifird = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.user.unsername 