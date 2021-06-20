from django.shortcuts import render
from django.http import HttpResponse

from .models import Pizza

import random

# Create your views here.
def index(request, pid):
    pizza = Pizza.objects.get(id=pid)
    return HttpResponse(
        content = {
            'id': pizza.id,
            'title': pizza.title,
            'description': pizza.description,
        }
    )

    if not pizza:
        return HttpResponse(
            content = {
                'status': "error",
                'message': "pizza not found",
            }
        )
    
def randompage(request):
    pizzas = Pizza.objects.all()
    pid = random.randint(0, len(pizzas))

    pizza = Pizza.objects.get(id=pid)
    return HttpResponse(
        content = {
            'id': pizza.id,
            'title': pizza.title,
            'description':pizza.description,
        }
    )