# Generated by Django 4.1.7 on 2023-07-01 12:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
