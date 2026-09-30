from django.db import models
from django.urls import reverse
# Create your models here.
class Creators(models.Model):
    title = models.CharField('Название', max_length=50)
    creator = models.CharField('Имя', max_length=250)
    full_text = models.TextField('Подробнее')
    date = models.DateTimeField('Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Создатель'
        verbose_name_plural = 'Создатели'

class New(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Подробнее')
    date = models.DateTimeField('Дата')
    # Ссылка на картинку, URLField проверяет формат
    image = models.URLField('Картинка (ссылка)', max_length=2083, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', args=[self.id])

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
