import datetime
import os.path

import requests
from django.urls import reverse_lazy
from django.views import generic

from .forms import FormImage
from .models import ModelImage


class ImagesView(generic.ListView, generic.FormView):
    form_class = FormImage
    success_url = reverse_lazy('index')

    model = ModelImage
    template_name = 'resize_image/index.html'
    context_object_name = 'images'
    queryset = ModelImage.objects.all().order_by('-date_added')

    def form_valid(self, form):
        link = form.cleaned_data.get('link')
        image = self.request.FILES.get('image')
        if link and image:
            self.form_invalid(form)
        if link:
            self._download_image_and_saved_in_db(link)
            return super().form_valid(form)
        elif image:
            print(image)
            self.model.objects.create(
                name=image.name,
                image=image
            )
            return super().form_valid(form)
        else:
            self.form_invalid(form)

    def _download_image_and_saved_in_db(self, link):
        p = requests.get(link)
        format = p.headers.get('Content-Type').split('/')[1]
        file_name = str(p.headers.get('Etag')).replace('"', '')

        current_date = datetime.datetime.utcnow()
        current_month = current_date.month if current_date.month > 9 else f'0{current_date.month}'
        current_day = current_date.day if current_date.day > 9 else f'0{current_date.day}'
        _path = os.path.normpath(f'media/images/{current_date.year}/{current_month}/{current_day}')

        if os.path.isdir(_path):
            with open(f'{_path}/{file_name}.{format}', 'wb') as out:
                out.write(p.content)
        else:
            os.makedirs(_path)

        path_for_db = os.path.normpath(f'images/{current_date.year}/{current_month}/{current_day}/{file_name}.{format}')
        self.model.objects.create(
            name=f'{file_name}.{format}',
            image=path_for_db
        )
