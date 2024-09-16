# Generated by Django 5.1.1 on 2024-09-16 02:10

import core.models
import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60, verbose_name='Nome do Livro')),
                ('arquivo', models.FileField(upload_to='livros/', validators=[core.models.validar_pdf], verbose_name='Arquivo PDF')),
                ('foto_livro', stdimage.models.StdImageField(blank=True, default=None, force_min_size=False, null=True, upload_to='books/', variations={'thumb': {'crop': True, 'height': 100, 'width': 100}})),
            ],
        ),
    ]
