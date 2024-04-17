from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    salary = models.FloatField()
    joining_date = models.DateField()
    class Meta:
        ordering = ['name']

# Create your models here.
