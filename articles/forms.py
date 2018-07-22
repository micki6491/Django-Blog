from django import forms
from .models import Article, Publication


class NewArticleForm(forms.ModelForm):
    publication = forms.ModelChoiceField(queryset=Publication.objects.all())

    subject = forms.CharField(
        label="What's the subject of your article?"
    )

    photo = forms.ImageField(
        label='Choose your image',
        help_text='The image should be 700x300.')

    message = forms.CharField(
        label="Write your article below",
        widget=forms.Textarea(
            attrs={'rows': 100, 'placeholder': 'What is on your mind?'}
        ),
        max_length=30000,
        help_text='Max length is set to 30000'
    )

    class Meta:
        model = Article
        fields = ['publication', 'subject', 'photo', 'message']
