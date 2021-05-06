from django import forms
from .models import ModelImage

class FormImage(forms.ModelForm):
    link = forms.URLField(required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = ModelImage
        fields = ('link', 'image')