# Generated by Django 4.1 on 2022-09-28 11:54

from django.db import migrations
import pictures.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_imagens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagens',
            name='foto',
            field=pictures.models.PictureField(aspect_ratios=[None], breakpoints={'l': 1200, 'm': 992, 's': 768, 'xl': 1400, 'xs': 576}, container_width=1200, file_types=['WEBP'], grid_columns=12, pixel_densities=[1, 2], upload_to='home/imagens'),
        ),
    ]
