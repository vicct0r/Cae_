# Generated by Django 5.1.1 on 2024-09-16 04:43

import stdimage.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='livros',
            options={'verbose_name': 'Livro', 'verbose_name_plural': 'Livros'},
        ),
        migrations.AlterField(
            model_name='livros',
            name='foto_livro',
            field=stdimage.models.StdImageField(blank=True, default=None, force_min_size=False, null=True, upload_to='books/', variations={'thumb': {'crop': True, 'height': 200, 'width': 200}}),
        ),
    ]
