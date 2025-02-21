from django.shortcuts import render
from .models import User
from .forms import UserRegistrationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class UserRegisterationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "forms/signup.html"
    success_url = reverse_lazy("login")
