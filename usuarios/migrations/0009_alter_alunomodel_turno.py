# Generated by Django 3.2.8 on 2024-09-09 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_auto_20240909_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunomodel',
            name='turno',
            field=models.CharField(choices=[('Horário Integral', 'Horario Integral'), ('Noturno', 'Noturno')], default='#', max_length=18, verbose_name='Turno'),
        ),
    ]
