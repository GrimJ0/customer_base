# Generated by Django 3.2 on 2022-01-20 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_client_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]