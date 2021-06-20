from django.shortcuts import render

# To authenticate the user with auth app provided with Django
from django.contrib.auth.forms import UserCreationForm # A form to sign in
from django.contrib.auth import login, authenticate
from django.views import View
from django.shortcuts import render, redirect

# Create your views here.
# Class based view
class SignupView(View):
    template_name = "signup.html"

    def get(self, request):
        return render(request, self.template_name, {'form':UserCreationForm()})

    def post(self, request):
        if form.is_valid():
            form.save()
            username = form.clened_data.get('username')
            password = form.cleaned_data.get("password")
            user = authenticate(
                username = username,
                password = password
            ) # Here we authenticate the user with the cleaned data
            login(request, user) #Login with the user that has authenticated
            return redirect("/")