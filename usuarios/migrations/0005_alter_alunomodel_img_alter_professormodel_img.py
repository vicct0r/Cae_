# Generated by Django 5.1 on 2024-08-30 20:25

import stdimage.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_alunomodel_img_alter_professormodel_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunomodel',
            name='img',
            field=stdimage.models.StdImageField(default='default/default_user.webp', force_min_size=False, upload_to='profiles/', variations={'thumb': {'crop': True, 'height': 460, 'width': 460}}, verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='professormodel',
            name='img',
            field=stdimage.models.StdImageField(default='default/default_user.webp', force_min_size=False, upload_to='profiles/', variations={'thumb': {'crop': True, 'height': 460, 'width': 460}}, verbose_name='Imagem'),
        ),
    ]
