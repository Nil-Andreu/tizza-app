from django.urls import path
from .views import index, randompage, TenPizzas

urlpatterns = [
    path('<int:pid>/', index, name="pizza"),
    path('random/', randompage, name="random" ),
    path('random10/', TenPizzas.as_view())
]