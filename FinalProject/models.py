from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class list(models.Model):
    Class=models.CharField(max_length=20)
    Techer=models.CharField(max_length=20)
    objects=models.Manager()
class Class(models.Model):
    Name=models.CharField(max_length=20)
    Division=models.CharField(max_length=20)
class Techer(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=40)
    Specialization=models.CharField(max_length=40)
