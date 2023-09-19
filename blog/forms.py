from django import forms

from blog.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        widgets = {
            "body": forms.Textarea(attrs={"style": "height: 30px; width: 300px;", "placeholder": "Add a comment..."}),
        }
