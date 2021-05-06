from django.db import models


class ModelImage(models.Model):
    image = models.ImageField(verbose_name='Изображение')
