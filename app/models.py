from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    """Модель клиента"""
    last_name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    phone = PhoneNumberField()
    price = models.IntegerField()
    count = models.IntegerField(default=1)
    black_list = models.BooleanField(default=False)
    addition = models.DateTimeField('Дата добавления', auto_now_add=True)
    updated = models.DateTimeField('Дата добавления', auto_now=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} - {self.phone}"

    def get_absolute_url(self):
        return reverse('home')