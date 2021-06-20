from django.apps import AppConfig

class PizzaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.pizza' #Put this in the configuration so it is recognized
