from django.contrib import admin
from .models import Like, SavedPost


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ["post", "user", "date"]


@admin.register(SavedPost)
class SavedPostAdmin(admin.ModelAdmin):
    list_display = ["post", "user"]
