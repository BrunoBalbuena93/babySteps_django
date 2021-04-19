from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    length = models.PositiveIntegerField()
    release_year = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title
    

class Customer(models.Model):
    name = models.CharField(max_length=40)
    last = models.CharField(max_length=80)
    phone = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name +  " " + self.last