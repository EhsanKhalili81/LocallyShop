# Generated by Django 4.1.7 on 2023-06-05 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_alter_userinformation_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='address',
            field=models.CharField(blank=True, default='-', max_length=255),
        ),
    ]