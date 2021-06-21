from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

import json
from django.contrib.auth.decorators import login_required

from .models import Pizza


import random

# A function that will get us the ip of our clients
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# django-ratelimit will allow us to limit the number of request received over a time

# The view for adding pizza to users who own a pizzeria.
# @ratelimit(key="ip", rate="100/h") We limit the amount of request an user can make
@login_required # The logged users will be able ot create a new pizza
def index(request, pid):
    if request.method == 'POST':
        data = json.loads(request.body) # Going to load in a json format the information loaded in body
        new_pizza = Pizza.objects.create(
            title = data['title'],
            description = data['description'],
            creator = request.user, #The user who requested the information, which is populated by AuthentificationMiddleware
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

class TenPizzas(View):
    template_name = 'ten_pizzas.html'

    def get(self,request):
        pizzas = Pizza.objects.order_by('?')[:10] # This will get 10 random pizzas as is orrdered randomly

        return render(request, self.template_name, {
            'pizzas':pizzas
        })

# Django has layers that you request and response goes through when they enter and exist your app
# - AuthentificationMiddleware: ensures that request.user object exist and you can access it.
# If the user is logged in then it will be populated with the user object. If not,
# then an anonymous user will be sitting on this attribute. Oftentimes it is very convenient
# to subclass this middleware and extend it with other user related data,
# such as from the UserProfile
# - SecurityMiddleware: provides various security related features, such as HTTP redirects, redirect blocking
# and xss protection.
# - CommonMiddleware: provides some basic functionalities tha tare chores to implement. Such
# as sending away banned user-agents and making sure that the URL ends up with a /
