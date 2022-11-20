from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = {
            "name",
            "price",
            "description",
            "image",
        }