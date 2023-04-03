from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User
# Create your models here.

class User(AbstractUser):
    is_admin=models.BooleanField('Is admin', default=False)
    is_owner=models.BooleanField('Is owner', default=False)
    is_tenant=models.BooleanField('Is tenant', default=False)


class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='listings')
