# Generated by Django 4.1.7 on 2023-07-09 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0006_alter_comments_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='malyat',
            field=models.PositiveBigIntegerField(default=0, null=True),
        ),
    ]
