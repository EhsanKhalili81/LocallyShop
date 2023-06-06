# Generated by Django 4.1.7 on 2023-06-05 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_alter_userinformation_kodeposti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='address',
            field=models.CharField(blank=True, default='-', max_length=255),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='tel',
            field=models.PositiveBigIntegerField(blank=True, default=0),
        ),
    ]
