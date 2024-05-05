from django import forms
from .models import Blog, Comment


class CreateUpdateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'status', 'image']


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
