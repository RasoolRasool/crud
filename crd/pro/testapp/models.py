from django.db import models

# Create your models here.
class Employee(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=10)
    name=models.CharField(max_length=20)
    salary=models.IntegerField()
    address=models.TextField(max_length=100)
