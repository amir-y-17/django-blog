from .models import Like, SavedPost
from blog.models import Post
from django.http import JsonResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


class LikePostView(LoginRequiredMixin, View):
    login_url = "users:login"

    def post(self, request, **kwargs):
        post = get_object_or_404(Post, id=kwargs.get("pk"))
        user = request.user

        like, created = Like.objects.get_or_create(post=post, user=user)
        if not created:
            # Unlike
            like.delete()
            liked = False
        else:
            # Like
            liked = True

        post_likes_count = post.likes.count()
        response_data = {"liked": liked, "likes_count": post_likes_count}
        return JsonResponse(response_data)


class SavePostView(LoginRequiredMixin, View):
    login_url = "users:login"

    def post(self, request, **kwargs):
        post = get_object_or_404(Post, id=kwargs.get("pk"))
        user = request.user

        saved_post, created = SavedPost.objects.get_or_create(post=post, user=user)
        if not created:
            saved_post.delete()
            saved = False
        else:
            saved = True

        return JsonResponse({"saved": saved})
