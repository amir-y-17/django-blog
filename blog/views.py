from .models import Category, Post
from django.contrib import messages
from .forms import CreateNewPostForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, DetailView


class CreateNewPostView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form = CreateNewPostForm(request.POST, request.FILES)
        user = request.user
        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.save()
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


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
