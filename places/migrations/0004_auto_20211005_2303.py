# Generated by Django 3.2.8 on 2021-10-05 23:03

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_place_description_short'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(verbose_name='Полное описание'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('order', models.IntegerField(verbose_name='Порядок')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.place', verbose_name='Место')),
            ],
        ),
    ]