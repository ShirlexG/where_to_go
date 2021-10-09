# Generated by Django 3.2.8 on 2021-10-05 19:08

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description_short', models.TextField(max_length=200, verbose_name='Краткое описание')),
                ('description_long', tinymce.models.HTMLField(verbose_name='Длинное описание')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('latitude', models.FloatField(verbose_name='Ширина')),
            ],
        ),
    ]