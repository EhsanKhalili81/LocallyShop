# Generated by Django 4.1.7 on 2023-06-28 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_remove_slider_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='Description',
        ),
    ]
