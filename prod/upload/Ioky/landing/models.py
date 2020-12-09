from django.db import models


class Question(models.Model):
    question = models.TextField('Текст вопроса')
    answer = models.TextField('Текст ответа', null=True, blank=True)
    mail = models.CharField('Почта спросившего', max_length=50, null=True, blank=True)
    name = models.CharField('Имя спросившего', max_length=100)
    check = models.BooleanField('Проверено/В проверке', default=False)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
