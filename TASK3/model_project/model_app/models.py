from django.db import models

# Create your models here.
class Student2(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField(max_length=10)
    Dte=models.DateField(max_length=10)

