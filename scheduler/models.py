import uuid
from django.db import models
from django.contrib.auth.models import User
 
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    phone = models.CharField(max_length=20)


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=200, null=False)
    provider = models.CharField(max_length=200, null=False)
    headquarter = models.IntegerField(max_length=10, null=True)
    address = models.CharField(max_length=249, null=False)


    
