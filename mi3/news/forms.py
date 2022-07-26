from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


# Связь create.html с БД (моделью Articles)
class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'annons', 'text', 'post_date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "annons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            "post_date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            })
        }