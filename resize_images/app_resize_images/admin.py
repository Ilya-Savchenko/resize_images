from django.contrib import admin
from .models import ModelImage


@admin.register(ModelImage)
class ModelImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')