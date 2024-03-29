# Generated by Django 4.1.7 on 2023-06-05 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='kodeposti',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='tel',
            field=models.PositiveBigIntegerField(blank=True, default=0),
        ),
    ]
