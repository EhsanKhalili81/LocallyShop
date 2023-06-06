# Generated by Django 4.1.7 on 2023-06-06 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0009_alter_userinformation_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='address',
            field=models.CharField(blank=True, default='-', max_length=255),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='kodeposti',
            field=models.PositiveBigIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='tel',
            field=models.PositiveBigIntegerField(blank=True, default=0),
        ),
    ]
