from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "password1": forms.PasswordInput(),
            "password2": forms.PasswordInput(),
        }

    def clean_username(self):
        username = self.cleaned_data.get("username")

        if not username:
            raise forms.ValidationError("Username is required!")

        if len(username) < 4:
            raise forms.ValidationError(
                "The username must be at least 4 characters long!"
            )

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username already exists!")

        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email already exists!")

        return email


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(
        max_length=16, widget=forms.PasswordInput(), required=True
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")

        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("The username does not exist.")
        return username
