# Generated by Django 3.0.7 on 2020-08-24 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_auto_20200824_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='blockLink',
            field=models.CharField(default='', max_length=300, verbose_name='Ссылка под блоком (url)'),
        ),
        migrations.AlterField(
            model_name='block',
            name='blockLinkAnimation',
            field=models.CharField(default='', max_length=50, verbose_name='Анимация кнопки (ссылки)'),
        ),
        migrations.AlterField(
            model_name='block',
            name='blockLinkAnimationDelay',
            field=models.SmallIntegerField(default='', verbose_name='Задержка анимации кнопки (ссылки)'),
        ),
        migrations.AlterField(
            model_name='block',
            name='blockLinkAnimationDuration',
            field=models.SmallIntegerField(default='', verbose_name='Длительность анимации кнопки (ссылки)'),
        ),
        migrations.AlterField(
            model_name='block',
            name='blockLinkBorderColor',
            field=models.CharField(default='none', max_length=50, verbose_name='Цвет границы кнопки (ссылки)'),
        ),
        migrations.AlterField(
            model_name='block',
            name='blockLinkText',
            field=models.CharField(default='', max_length=50, verbose_name='Текст кнопки (ссылки)'),
        ),
        migrations.AlterField(
            model_name='block',
            name='blockLinkTextColor',
            field=models.CharField(default='none', max_length=50, verbose_name='Цвет текста кнопки (ссылки)'),
        ),
    ]