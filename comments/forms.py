from django import forms


class CommentForm(forms.Form):
    content = forms.CharField(
        max_length=500, widget=forms.Textarea(), label="Comment", required=True
    )

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if not content:
            raise forms.ValidationError("This field is required.")
        if len(content) > 500:
            raise forms.ValidationError("Comment cannot exceed 500 characters.")
        return content
