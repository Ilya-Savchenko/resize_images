# Generated by Django 2.2 on 2021-05-08 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_resize_images', '0003_modelimage_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelimage',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
