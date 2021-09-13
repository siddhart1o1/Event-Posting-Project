from enum import auto
from os import times
from django.db import models
from django.contrib.auth.models import User
from django.db.models.expressions import Value
from django.db.models.fields.related import ForeignKey
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=False,auto_now_add=False,blank=False)
    time = models.TimeField(auto_now=False, auto_now_add=False,blank=False)
    location = models.CharField(max_length=150)
    image= models.ImageField(null=True,blank = True)
    Liked=models.ManyToManyField(User,default=None,blank=True,related_name="Liked")

    def __str__(self):
        return str(self.title)
    
    @property
    def num_Liked(self):
        return self.Liked.all().count()

LIKE_CHOICES = (
    ("Like" , "Like"),("UnLike","UnLike"),
)

class Like(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,default="Like",max_length=10)

    def _str_(self):
        return str(self.post)
