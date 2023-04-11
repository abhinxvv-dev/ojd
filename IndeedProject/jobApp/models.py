from django.db import models

# Create your models here.
class hydjobs(models.Model):
    id=models.IntegerField(primary_key=True)
    company=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    date=models.DateField()

class lkojobs(models.Model):
    id=models.IntegerField(primary_key=True)
    company=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    date=models.DateField()
