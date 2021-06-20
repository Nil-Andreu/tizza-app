from django.shortcuts import render
from django.http import HttpResponse

from .models import Pizza

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