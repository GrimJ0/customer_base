from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    """Модель клиента"""
    last_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Имя')
    first_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Фамилия')
    phone = PhoneNumberField(verbose_name='Телефон')
    price = models.IntegerField(verbose_name='Прайс')
    count = models.IntegerField(default=1, verbose_name='Количество посещений')
    black_list = models.BooleanField(default=False, verbose_name='Черный список')
    addition = models.DateTimeField('Дата добавления', auto_now_add=True)
    updated = models.DateTimeField('Дата последнего посещения', auto_now=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} - {self.phone}"

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        ordering = ['-updated']