from django.db import models
#from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager




class User(AbstractBaseUser):
    username=models.CharField(max_length=100,blank=True,null=True)
    password=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    whatsapp=models.IntegerField(blank=True,null=True)
    instagram=models.URLField(max_length=100,blank=True,null=True)
    twitter=models.URLField(max_length=100,blank=True,null=True)
    facebook=models.URLField(max_length=100,blank=True,null=True)
    address=models.CharField(max_length=100,blank=True,null=True)
    USERNAME_FIELD = 'email'



