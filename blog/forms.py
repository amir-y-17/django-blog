from django import forms
from .models import Post, Category


class CreateNewPostForm(forms.ModelForm):
    image1 = forms.ImageField(required=True)
    image2 = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ["title", "description", "category", "image1", "image2"]
