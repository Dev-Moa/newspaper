from django import forms
from .models import Comment  # comment table
# 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment", "author")