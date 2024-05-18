from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    telephone_number = models.CharField(max_length=12)

def _str_(self):
    return self.first_name


class Event(models.Model):
    location = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    Amount = models.IntegerField(default=0)
    Date=models.DateField(auto_now=True)
    Hours= models.DateTimeField(blank=True, null=True)
    # amount = models.IntegerField(max_length=6)

def _str_(self):
    return self.location
    
class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=12)
    Amount = models.CharField(max_length=6)
    Payment_Options= models.CharField(max_length=50)

def _str_(self):
    return self.first_name



# Create your models here.
