from django.db import models

# Create your models here.
class Pizza(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=300)