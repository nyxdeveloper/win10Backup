# Generated by Django 3.0.7 on 2020-08-24 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='img',
            field=models.ImageField(blank=True, upload_to='blocks_image', verbose_name='Фото блока'),
        ),
    ]
