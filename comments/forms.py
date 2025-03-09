from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if not content:
            raise forms.ValidationError("This field is required.")
        if len(content) > 500:
            raise forms.ValidationError("Comment cannot exceed 500 characters.")
        return content
