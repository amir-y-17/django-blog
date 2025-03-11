from django.urls import path
from . import views


app_name = "intractions"

urlpatterns = [
    path("Like/post-<int:pk>/", views.LikePostView.as_view(), name="like_post"),
    path("save/post-<int:pk>/", views.SavePostView.as_view(), name="save_post"),
]
