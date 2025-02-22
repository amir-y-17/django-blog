from django.shortcuts import render, redirect
from .models import User
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


class UserRegisterationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "forms/signup.html"
    success_url = reverse_lazy("users:login")


class UserLoginView(View):
    def get(self, request):
        # Use a single form instance without unnecessary repetition.
        return render(request, "forms/login.html", {"form": UserLoginForm()})

    def post(self, request):
        form = UserLoginForm(request.POST)

        if not form.is_valid():
            messages.error(request, "Please check your login details and try again.")
            return redirect("users:login")

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(
                request, "The username or password you entered is incorrect."
            )
            return redirect("users:login")

        if not user.is_active:
            messages.error(request, "Your account is inactive. Please contact support.")
            return redirect("users:register")

        # If authentication is successful and user is active
        login(request, user)
        messages.success(request, "Welcome back! You have logged in successfully.")
        return redirect("blog:home")
