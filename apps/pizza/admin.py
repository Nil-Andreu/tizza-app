from django.contrib import admin
from .models import Pizzeria, Pizza, Likes

# Register your models here.
admin.site.register(Pizzeria)
admin.site.register(Pizza)
admin.site.register(Likes)