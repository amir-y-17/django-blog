from django.urls import path
from . import views


app_name = "comments"

urlpatterns = [
    path(
        "post-<int:pk>/new-comment/", views.NewCommentView.as_view(), name="new_comment"
    ),
    path(
        "post-<int:pk>/all-comments/",
        views.CommentsListView.as_view(),
        name="all_comments",
    ),
]
