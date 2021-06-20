from django.urls import path
from .views import index, randompage

urlpatterns = [
    path('<int:pid>', index, name="pizza"),
    path('random/', randompage, name="random" ),
]