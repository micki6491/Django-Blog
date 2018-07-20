from django import forms
from .models import Article


class NewArticleForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 100, 'placeholder': 'What is on your mind?'}
        ),
        max_length=30000,
        help_text='Max length is set to 30000'
    )

    class Meta:
        model = Article
        fields = ['subject', 'message', ]
