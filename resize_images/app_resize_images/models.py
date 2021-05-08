from django.db import models


class ModelImage(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='images/%Y/%m/%d/')
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
