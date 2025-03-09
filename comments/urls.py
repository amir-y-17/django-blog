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
    path(
        "edit-comment/<int:comment_id>/",
        views.EditCommentView.as_view(),
        name="edit_comment",
    ),
    path(
        "delete-comment/<int:pk>/",
        views.DeleteCommentView.as_view(),
        name="delete_comment",
    ),
]
