from django.views import generic

from .forms import FormImage
from .models import ModelImage


class ImagesView(generic.ListView, generic.FormView):
    form_class = FormImage
    model = ModelImage
    template_name = 'resize_image/index.html'