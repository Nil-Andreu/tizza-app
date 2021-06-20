from django.urls import path
from .views import index

urlpatterns = [
    path('<int: pid>', index, name="pizza")
]