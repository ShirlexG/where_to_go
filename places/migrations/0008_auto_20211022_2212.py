# Generated by Django 3.2.8 on 2021-10-22 22:12

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_auto_20211016_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='order',
            field=models.IntegerField(blank=True, default=0, verbose_name='Порядок'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.CharField(blank=True, max_length=400, verbose_name='Краткое описание'),
        ),
    ]
