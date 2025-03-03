from django.contrib import admin
from .models import Category, Post, PostImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ["name"]}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "author", "created_at"]
    list_filter = ["category", "author"]


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ["post"]
