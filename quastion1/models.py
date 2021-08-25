from django.db import models


# Create your models here.
class Student(models.Model):
       firstname=models.CharField(max_length=40)
       lastname=models.CharField(max_length=40)
       UniversityName=models.CharField(max_length=30)
class UniversityName(models.Model):
       UniversityID=models.FloatField()
       doctorsname=models.CharField(max_length=40)