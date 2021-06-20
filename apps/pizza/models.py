from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pizzeria(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=120, blank=False)
    phone = models.CharField(max_length=40)

class Pizza(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=300)
    url = models.URLField(null = True, blank=True)
    approved = models.BooleanField(default=False)
    creator = models.ForeignKey(Pizzeria, on_delete=models.CASCADE)

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Using User model as a foreign key is more stable practice than using the User model, it is more flexible
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)