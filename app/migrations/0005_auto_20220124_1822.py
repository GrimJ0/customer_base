# Generated by Django 3.2 on 2022-01-24 15:22

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_client_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['-updated']},
        ),
        migrations.AlterField(
            model_name='client',
            name='black_list',
            field=models.BooleanField(default=False, verbose_name='Черный список'),
        ),
        migrations.AlterField(
            model_name='client',
            name='count',
            field=models.IntegerField(default=1, verbose_name='Количество посещений'),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='client',
            name='price',
            field=models.IntegerField(verbose_name='Прайс'),
        ),
        migrations.AlterField(
            model_name='client',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего посещения'),
        ),
    ]
