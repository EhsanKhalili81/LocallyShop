# Generated by Django 4.1.7 on 2023-06-19 10:30

import Core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=Core.models.file_path),
        ),
    ]