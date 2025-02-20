from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ["username", "first_name", "last_name", "email"]
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional Info",
            {"fields": ("about_me", "date_of_birth", "profile_image")},
        ),
    )
