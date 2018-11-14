from django.db import models

# Create your models here.

class Country(models.Model):
    code = models.TextField()
    name = models.CharField(max_length=100, blank=True, default='')

class State(models.Model):
    country_id = models.ForeignKey(Country, related_name='states', on_delete=models.CASCADE)
    code = models.TextField()
    name = models.CharField(max_length=100, blank=True, default='')