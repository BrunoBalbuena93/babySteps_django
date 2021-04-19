from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    
    
    def get_absolute_url(self):
        return reverse("das_app:detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name="students", on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    
    