# Imports
from .models import Comment
from django import forms

# Form for comment message
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("message",)

