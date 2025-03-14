from .models import User
from blog.models import Post
from intractions.models import SavedPost
from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import (
    UserRegistrationForm,
    UserLoginForm,
    UserEditForm,
    UserPasswordChangeForm,
)


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


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "users/profile.html"
    login_url = "users:login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent_posts"] = Post.objects.filter(author=self.request.user)[:4]
        return context


class EditProfileView(View, LoginRequiredMixin):
    def get(self, request):
        form = EditProfileView(instance=request.user)
        context = {"form": form}
        return render(request, "users/edit_profile.html", context)

    def post(self, request):
        form = UserEditForm(request.POST, instance=request.user, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect("users:profile")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return render(request, "users/edit_profile.html", {"form": form})


class UserPasswordChangeView(LoginRequiredMixin, View):
    def post(self, request):
        form = UserPasswordChangeForm(
            user=request.user, data=request.POST
        )  # Specify the user
        if form.is_valid():
            try:
                user = form.save()
                update_session_auth_hash(request, user)  # Keep the user logged in
                messages.success(
                    request, "Your password has been successfully changed."
                )
                return redirect("users:password_change_done")
            except Exception as e:
                messages.error(
                    request,
                    "An error occurred while changing your password. Please try again.",
                )
                return render(
                    request, "registration/change_password.html", {"form": form}
                )
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(
                        request, f"{field}: {error}"
                    )  # Display the error to the user
            return render(request, "registration/change_password.html", {"form": form})

    def get(self, request):
        form = UserPasswordChangeForm(user=request.user)
        return render(request, "registration/change_password.html", {"form": form})


class MyPostsPageView(LoginRequiredMixin, TemplateView):
    template_name = "users/posts_page.html"
    login_url = "users:login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context


class MySavedPostsPageView(LoginRequiredMixin, TemplateView):
    login_url = "users:login"
    template_name = "users/saved_posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["saved_posts"] = SavedPost.objects.filter(user=self.request.user)
        print(context["saved_posts"])
        return context
