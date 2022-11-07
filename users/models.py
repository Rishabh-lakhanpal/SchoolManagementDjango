from django.db import models

# Create your models here.
class stud(models.Model):
    Name = models.CharField(max_length=30)
    Classroom = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)
    School = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)