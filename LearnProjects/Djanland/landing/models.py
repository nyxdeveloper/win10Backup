from django.db import models

class Config(models.Model):
    name = models.CharField('Название конфигурации', max_length=50)

class Block(models.Model):
    img = models.ImageField('Фото блока', upload_to='blocks_image', blank=True)
    title = models.CharField('Заголовок блока', max_length=150)
    titleSize = models.SmallIntegerField('Размер шрифта заголовка')
    text = models.TextField('Текст блока')
    textColor = models.CharField('Цвет текста', max_length=50)
    textSize = models.SmallIntegerField('Размер шрифта текста')
    blockID = models.CharField('Идентификатор блока', max_length=50)
    blockLink = models.CharField('Ссылка под блоком (url)', max_length=300, default='')
    blockLinkText = models.CharField('Текст кнопки (ссылки)', max_length=50, default='')
    blockLinkTextColor = models.CharField('Цвет текста кнопки (ссылки)', max_length=50, default='none')
    blockLinkBorderColor = models.CharField('Цвет границы кнопки (ссылки)', max_length=50, default='none')
    blockLinkAnimation = models.CharField('Анимация кнопки (ссылки)', max_length=50, default='')
    blockLinkAnimationDuration = models.SmallIntegerField('Длительность анимации кнопки (ссылки)', default='')
    blockLinkAnimationDelay = models.SmallIntegerField('Задержка анимации кнопки (ссылки)', default='')
    blockAnimation = models.CharField('Анимация блока', max_length=50)
    titleAnimation = models.CharField('Анимация заголовка', max_length=50)
    textAnimation = models.CharField('Анимаци текста', max_length=50)
    blockAnimationDuration = models.SmallIntegerField('Длительность анимации блока')
    titleAnimationDuration = models.SmallIntegerField('Длительность анимации заголовка')
    textAnimationDuration = models.SmallIntegerField('Длительность анимации текста')
    blockAnimationDelay = models.SmallIntegerField('Задержка анимации блока')
    titleAnimationDelay = models.SmallIntegerField('Задержка анимации заголовка')
    textAnimationDelay = models.SmallIntegerField('Задержка анимации текста')

    @property
    def photo_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'


class HeadersLink(models.Model):
    href = models.CharField('URl', max_length=150)
    text = models.CharField('Текст', max_length=50)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ссылка в шапке'
        verbose_name_plural = 'Ссылка в шапке'


class Header(models.Model):
    brand = models.CharField('Заголовок сайта', max_length=100)
    color = models.CharField('Цвет текста', max_length=50)
    background = models.CharField('Цвет фона', max_length=50)

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'Шапка'
        verbose_name_plural = 'Шапки'


class Footer(models.Model):
    brand = models.CharField('Заголовок подвала', max_length=100)
    year = models.PositiveSmallIntegerField('Год')

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'Подвал'
        verbose_name_plural = 'Подвалы'
