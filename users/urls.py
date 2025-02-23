from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "users"
urlpatterns = [
    path("register/", views.UserRegisterationView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    # Reset Password URLs
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(success_url="done"),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(success_url="complete"),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/MQ/set-password/complete/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
