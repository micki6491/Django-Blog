from django import forms
from .models import Article


class NewArticleForm(forms.ModelForm):
    category = forms.ChoiceField(
        label="Choose a category",
        choices=[('Tips', 'Tips',), ('News', 'News',), ('Tutorials', 'Tutorials',)]
    )

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
        fields = ['category','subject', 'photo', 'message']
