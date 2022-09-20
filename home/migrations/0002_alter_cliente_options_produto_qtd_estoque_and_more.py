# Generated by Django 4.1 on 2022-08-24 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['-nome']},
        ),
        migrations.AddField(
            model_name='produto',
            name='qtd_estoque',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
