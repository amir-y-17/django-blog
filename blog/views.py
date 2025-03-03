from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Post, PostImage
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateNewPostForm
from django.urls import reverse_lazy
from django.contrib import messages


class CreateNewPostView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form = CreateNewPostForm(request.POST, request.FILES)
        user = request.user
        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.save()

            # Handle images
            for image in ["image1", "image2"]:
                img = form.cleaned_data.get(image)
                if img:
                    PostImage.objects.create(post=post, image=img)

            messages.success(request, "Post created successfully")
            return redirect("blog:home")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return render(
                request,
                "blog/new_post.html",
                {"form": form, "categories": Category.objects.all()},
            )

    def get(self, request, *args, **kwargs):
        form = CreateNewPostForm()
        categories = Category.objects.all()
        return render(
            request, "blog/new_post.html", {"form": form, "categories": categories}
        )
