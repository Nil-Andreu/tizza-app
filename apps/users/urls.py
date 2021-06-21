from django.urls import re_path
from .views import SignupView

urlpatterns = [
    re_path(r'register/$', SignupView.as_view()), # With as_view we can convert the class based view to a regular one
]