# Generated by Django 3.2.8 on 2024-09-09 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_alter_conta_nome_completo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conta',
            name='cargo',
        ),
        migrations.AddField(
            model_name='conta',
            name='multado',
            field=models.BooleanField(default=False, verbose_name='Multado'),
        ),
    ]
