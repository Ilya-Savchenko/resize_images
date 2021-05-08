from django import forms

from .models import ModelImage


class FormImage(forms.ModelForm):
    link = forms.URLField(required=False, help_text='Ссылка на изображение')
    image = forms.ImageField(required=False, help_text='Изображение на устройстве')

    class Meta:
        model = ModelImage
        fields = ('link', 'image')
