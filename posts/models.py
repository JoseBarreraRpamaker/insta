
from typing import cast
from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import create_many_to_many_intermediary_model


from users.models import Profile


class Post(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile ,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class tableOne(models.Model):
    pass

def __str__(self):
    return {'{}by @{}'.format(self.title,self.user.username)}

