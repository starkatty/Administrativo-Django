from django import forms
from .models import Post

class PostForm (forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'author',
            'title',
            'text',
            'created_date',
            'published_date',
        )
        labels={
            'author': 'Author:',
            'title': 'Title:',
            'text': 'Text:',
            'created_date': 'Created date:',
            'published_date': 'Published date:',
        } 