# Generated by Django 4.0.3 on 2022-03-04 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PreRest', '0003_alter_respuesta_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preguntas',
            name='respuesta',
        ),
        migrations.AddField(
            model_name='respuesta',
            name='pregunta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PreRest.preguntas'),
        ),
    ]