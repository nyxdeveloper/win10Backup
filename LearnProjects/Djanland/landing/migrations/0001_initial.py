# Generated by Django 3.0.7 on 2020-08-24 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='blocks_image', verbose_name='Фото блока')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок блока')),
                ('titleSize', models.SmallIntegerField(verbose_name='Размер шрифта заголовка')),
                ('text', models.TextField(verbose_name='Текст блока')),
                ('textColor', models.CharField(max_length=50, verbose_name='Цвет текста')),
                ('textSize', models.SmallIntegerField(verbose_name='Размер шрифта текста')),
                ('blockID', models.CharField(max_length=50, verbose_name='Идентификатор блока')),
                ('blockLink', models.CharField(default=None, max_length=300, verbose_name='Ссылка под блоком (url)')),
                ('blockLinkText', models.CharField(default=None, max_length=50, verbose_name='Текст кнопки (ссылки)')),
                ('blockLinkAnimation', models.CharField(default=None, max_length=50, verbose_name='Анимация кнопки (ссылки)')),
                ('blockLinkAnimationDuration', models.SmallIntegerField(default=None, verbose_name='Длительность анимации кнопки (ссылки)')),
                ('blockLinkAnimationDelay', models.SmallIntegerField(default=None, verbose_name='Задержка анимации кнопки (ссылки)')),
                ('blockAnimation', models.CharField(max_length=50, verbose_name='Анимация блока')),
                ('titleAnimation', models.CharField(max_length=50, verbose_name='Анимация заголовка')),
                ('textAnimation', models.CharField(max_length=50, verbose_name='Анимаци текста')),
                ('blockAnimationDuration', models.SmallIntegerField(verbose_name='Длительность анимации блока')),
                ('titleAnimationDuration', models.SmallIntegerField(verbose_name='Длительность анимации заголовка')),
                ('textAnimationDuration', models.SmallIntegerField(verbose_name='Длительность анимации текста')),
                ('blockAnimationDelay', models.SmallIntegerField(verbose_name='Задержка анимации блока')),
                ('titleAnimationDelay', models.SmallIntegerField(verbose_name='Задержка анимации заголовка')),
                ('textAnimationDelay', models.SmallIntegerField(verbose_name='Задержка анимации текста')),
            ],
            options={
                'verbose_name': 'Блок',
                'verbose_name_plural': 'Блоки',
            },
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100, verbose_name='Заголовок подвала')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Год')),
            ],
            options={
                'verbose_name': 'Подвал',
                'verbose_name_plural': 'Подвалы',
            },
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100, verbose_name='Заголовок сайта')),
                ('color', models.CharField(max_length=50, verbose_name='Цвет текста')),
                ('background', models.CharField(max_length=50, verbose_name='Цвет фона')),
            ],
            options={
                'verbose_name': 'Шапка',
                'verbose_name_plural': 'Шапки',
            },
        ),
        migrations.CreateModel(
            name='HeadersLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('href', models.CharField(max_length=150, verbose_name='URl')),
                ('text', models.CharField(max_length=50, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Ссылка в шапке',
                'verbose_name_plural': 'Ссылка в шапке',
            },
        ),
    ]
