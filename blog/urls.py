from django.urls import path
from django.views.generic import TemplateView

app_name = "blog"


urlpatterns = [
    path("home/", TemplateView.as_view(template_name="blog/home.html"), name="home"),
]
