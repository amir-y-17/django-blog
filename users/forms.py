from django import forms
from .models import User


class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(
        max_length=16,
        widget=forms.PasswordInput(),
        required=True,
        label="Confirm password",
    )

    class Meta:
        model = User
        fields = ["username", "email", "password", "confirm_password"]

    def clean_confirm_password(self):
        cd = self.cleaned_data
        password = cd.get("password")
        confirm_password = cd.get("confirm_password")

        if not password or not confirm_password:
            raise forms.ValidationError("Password and Confirm password are required!")

        if password != confirm_password:
            raise forms.ValidationError(
                "The password and its confirmation do not match."
            )

        return confirm_password

    def clean_username(self):
        cd = self.cleaned_data
        username = cd.get("username")

        # Check if the username is provided
        if not username:
            raise forms.ValidationError("username is required!")

        # Check if the username is at least 4 characters long
        if len(username) < 4:
            raise forms.ValidationError(
                "The username must be at least 4 characters long!"
            )

        # Check if the username already exists in the database
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username already exists!")

        return username

    def clean_email(self):
        cd = self.cleaned_data
        email = cd.get("email")

        # If an email is provided, check if it already exists in the database
        if email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("This email already exists!")

        return email
