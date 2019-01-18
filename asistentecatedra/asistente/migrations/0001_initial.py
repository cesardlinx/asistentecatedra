# Generated by Django 2.0.7 on 2018-12-29 02:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planificaciones', '0072_auto_20180929_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('archivo', models.FileField(null=True, upload_to='libros/', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='')),
                ('asignatura', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='libros', to='planificaciones.Asignatura')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libros', to='planificaciones.Curso')),
            ],
            options={
                'verbose_name_plural': 'libros',
                'db_table': 'libros',
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=92)),
                ('answer', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'preguntas',
                'db_table': 'preguntas',
            },
        ),
    ]