from django.urls import path
from .views import index, RandomPage, TenPizzas

urlpatterns = [
    path('<int:pid>/', index, name="pizza"),
    path('random/', RandomPage.as_view()),
    path('random10/', TenPizzas.as_view())
]