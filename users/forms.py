from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm


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


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "about_me",
            "date_of_birth",
            "profile_image",
        ]

    def clean_username(self):
        username = self.cleaned_data.get("username")

        if not username:
            raise forms.ValidationError("Username is required!")

        if len(username) < 4:
            raise forms.ValidationError(
                "The username must be at least 4 characters long!"
            )

        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This username already exists!")

        return username


class UserPasswordChangeForm(PasswordChangeForm):
    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password")
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                "Your old password was entered incorrectly. Please enter it again."
            )
        return old_password

    def clean_new_password2(self):
        new_password1 = self.cleaned_data.get("new_password1")
        new_password2 = self.cleaned_data.get("new_password2")

        # Check if both new passwords match
        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError("The two password fields didn't match.")

        # Optionally add more checks for password strength here

        return new_password2
