# Generated by Django 4.1.7 on 2023-07-01 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_remove_card_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='FunctionToDo',
            field=models.TextField(default='', null=True),
        ),
    ]
