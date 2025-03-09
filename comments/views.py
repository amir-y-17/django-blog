from .models import Comment
from blog.models import Post
from users.models import User
from .forms import CommentForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView, ListView
from django.shortcuts import render, redirect, get_object_or_404


class CommentsListView(TemplateView):
    template_name = "comments/comments_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = kwargs.get("pk")
        post = get_object_or_404(Post, id=post_id)
        comments = Comment.objects.filter(post=post)
        context["post"] = post
        context["comments"] = comments
        return context


class NewCommentView(LoginRequiredMixin, View):
    login_url = "users:login"

    def post(self, request, **kwargs):
        post = get_object_or_404(Post, id=kwargs.get("pk"))
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Comment.objects.create(
                post=post, author=request.user, content=cd["content"]
            )
            messages.success(request, "Your comment has been posted successfully.")
            return redirect("comments:all_comments", pk=kwargs.get("pk"))
        else:
            messages.error(
                request, "There was an error with your comment. Please try again."
            )
            return render(
                request, "comments/new_comment.html", {"form": form, "post": post}
            )
