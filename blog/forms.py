from django import forms

from .models import Comment

class CommentFrom(forms.ModelForm):
    class meta:
        model = Comment
        fields = ['name','email','body']
        