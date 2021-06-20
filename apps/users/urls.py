from django.urls import path
from .views import SignupView

urlpatterns = [
    path(r'^register/$', SignupView.as_view()), # With as_view we can convert the class based view to a regular one
]