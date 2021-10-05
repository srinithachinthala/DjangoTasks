from django.db import models

# Create your models here.
class BusTable(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=20)
    Email=models.EmailField()
    Password=models.CharField(max_length=20)
    Phone=models.IntegerField()
    Doj=models.DateField()
    From=models.CharField(max_length=20)
    To=models.CharField(max_length=20)