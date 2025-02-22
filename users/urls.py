from django.urls import path
from . import views


app_name = "users"
urlpatterns = [
    path("register/", views.UserRegisterationView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
]
