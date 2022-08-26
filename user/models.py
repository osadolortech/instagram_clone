from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=125,unique=True)
    name = models.CharField(max_length=125)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return self.username




def upload_to(instance, filename):
    return 'image/{filename}'.format(filename=filename)


class Profile(models.Model):
    user = models.OneToOneField(User,related_name='user_profile',on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to=upload_to,default='image/default.jpg')
    bio = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

