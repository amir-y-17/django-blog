from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "blog"


urlpatterns = [
    path("home/", views.HomePageView.as_view(), name="home"),
    path("new-post/", views.CreateNewPostView.as_view(), name="new_post"),
    path("posts/", views.PostListView.as_view(), name="post_list"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("edit-post/<int:pk>/", views.EditPostView.as_view(), name="edit_post"),
    path("delete-post/<int:pk>/", views.DeletePostView.as_view(), name="delete_post"),
]
