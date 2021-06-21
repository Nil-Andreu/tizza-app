from django.shortcuts import render
from django.http import HttpResponse

import json
from django.contrib.auth.decorators import login_required

from .models import Pizza

import random

# The view for adding pizza to users who own a pizzeria.
@login_required # The logged users will be able ot create a new pizza
def index(request, pid):
    if request.method == 'POST':
        data = json.loads(request.body) # Going to load in a json format the information loaded in body
        new_pizza = Pizza.objects.create(
            title = data['title'],
            description = data['description'],
            creator = request.user, #The user who requested the information
        )
        new_pizza.save()
        return HttpResponse(
            content={
                'id':new_pizza.id, # Accessing properties of the new pizza created
                'title':new_pizza.title,
                'description':new_pizza.description
            }
        )

    else:
        pizza = Pizza.objects.get(id=pid)
        return HttpResponse(
            content = {
                'id': pizza.id,
                'title': pizza.title,
                'description': pizza.description
            }
        )


    # pizza = Pizza.objects.get(id=pid)
    # return HttpResponse(
    #     content = {
    #        'id': pizza.id,
    #        'title': pizza.title,
    #        'description': pizza.description,
    #    }
    #)

    #if not pizza:
    #    return HttpResponse(
    #       content = {
    #            'status': "error",
    #            'message': "pizza not found",
    #        }
    #    )
    
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