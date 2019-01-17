from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

# CreateView ::A view that displays a form for creating an object,
# redisplaying the form with validation errors

class SignUp(generic.CreateView):
    form_class = UserCreationForm           # user form
    success_url = reverse_lazy('login')     # if successfully signed up go to login page
    template_name = 'signup.html'           # else  redirect to same page
