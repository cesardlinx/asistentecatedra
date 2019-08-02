# Generated by Django 2.2.1 on 2019-08-02 16:41

import ckeditor.fields
import ckeditor_uploader.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'áreas',
                'db_table': 'areas',
            },
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignaturas', to='planificaciones.Area')),
            ],
            options={
                'verbose_name_plural': 'asignaturas',
                'db_table': 'asignaturas',
            },
        ),
        migrations.CreateModel(
            name='BloqueCurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_bloque', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)])),
                ('name', models.CharField(max_length=70)),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bloques', to='planificaciones.Asignatura')),
            ],
            options={
                'verbose_name_plural': 'bloques curriculares',
                'db_table': 'bloques_curriculares',
            },
        ),
        migrations.CreateModel(
            name='CriterioEvaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=700)),
                ('codigo', models.CharField(max_length=15)),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='criterios_evaluacion', to='planificaciones.Asignatura')),
            ],
            options={
                'verbose_name_plural': 'criterios de evaluación',
                'db_table': 'criterios_evaluacion',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'cursos',
                'db_table': 'cursos',
            },
        ),
        migrations.CreateModel(
            name='Destreza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=400)),
                ('codigo', models.CharField(max_length=15)),
                ('imprescindible', models.BooleanField(default=False)),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destrezas', to='planificaciones.Asignatura')),
                ('bloque', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destrezas', to='planificaciones.BloqueCurricular')),
            ],
            options={
                'verbose_name_plural': 'destrezas',
                'db_table': 'destrezas',
            },
        ),
        migrations.CreateModel(
            name='ElementoCurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conocimientos_asociados', models.TextField(max_length=200)),
                ('actividades_evaluacion', models.TextField(max_length=200)),
                ('destreza', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='elementos_curriculares', to='planificaciones.Destreza')),
            ],
            options={
                'verbose_name_plural': 'elementos curriculares',
                'db_table': 'elementos_curriculares',
            },
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'niveles',
                'db_table': 'niveles',
            },
        ),
        migrations.CreateModel(
            name='Objetivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=620)),
                ('codigo', models.CharField(max_length=12)),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objetivos', to='planificaciones.Asignatura')),
            ],
            options={
                'verbose_name_plural': 'objetivos',
                'db_table': 'objetivos',
            },
        ),
        migrations.CreateModel(
            name='ObjetivoGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=420)),
                ('codigo', models.CharField(max_length=12)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objetivos_generales', to='planificaciones.Area')),
            ],
            options={
                'verbose_name_plural': 'objetivos generales',
                'db_table': 'objetivos_generales',
            },
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_unidad', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('titulo', models.CharField(max_length=400)),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unidades', to='planificaciones.Asignatura')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unidades', to='planificaciones.Curso')),
                ('objetivos', models.ManyToManyField(blank=True, related_name='unidades', to='planificaciones.Objetivo')),
                ('objetivos_generales', models.ManyToManyField(blank=True, related_name='unidades', to='planificaciones.ObjetivoGeneral')),
            ],
            options={
                'verbose_name_plural': 'unidades',
                'db_table': 'unidades',
            },
        ),
        migrations.CreateModel(
            name='Subnivel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('nivel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subniveles', to='planificaciones.Nivel')),
            ],
            options={
                'verbose_name_plural': 'subniveles',
                'db_table': 'subniveles',
            },
        ),
        migrations.CreateModel(
            name='ProcesoDidactico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('tiempo', models.CharField(max_length=11)),
                ('recursos', models.TextField(max_length=200)),
                ('elemento_curricular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procesos_didacticos', to='planificaciones.ElementoCurricular')),
            ],
            options={
                'verbose_name_plural': 'procesos didácticos',
                'db_table': 'procesos_didacticos',
            },
        ),
        migrations.CreateModel(
            name='PlanUnidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=50)),
                ('docentes', models.CharField(max_length=255)),
                ('paralelos', models.CharField(max_length=20)),
                ('aprobado_por', models.CharField(blank=True, max_length=50, null=True)),
                ('revisado_por', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('observaciones', models.TextField(blank=True, max_length=200, null=True)),
                ('ano_lectivo', models.CharField(max_length=9)),
                ('periodos', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31'), (32, '32'), (33, '33'), (34, '34'), (35, '35'), (36, '36'), (37, '37'), (38, '38'), (39, '39'), (40, '40')], default=1, validators=[django.core.validators.MaxValueValidator(40)])),
                ('tiempo', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31'), (32, '32'), (33, '33'), (34, '34'), (35, '35'), (36, '36'), (37, '37'), (38, '38'), (39, '39'), (40, '40')], default=1, validators=[django.core.validators.MaxValueValidator(40)])),
                ('necesidad_adaptacion', models.TextField(blank=True, max_length=600, null=True)),
                ('adaptacion_curricular', models.TextField(blank=True, max_length=600, null=True)),
                ('asignatura', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='planes_unidad', to='planificaciones.Asignatura')),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='planes_unidad', to='planificaciones.Curso')),
                ('elaborado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planes_unidad', to=settings.AUTH_USER_MODEL)),
                ('objetivos', models.ManyToManyField(blank=True, related_name='planes_unidad', to='planificaciones.Objetivo')),
                ('objetivos_generales', models.ManyToManyField(blank=True, related_name='planes_unidad', to='planificaciones.ObjetivoGeneral')),
                ('unidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='planes_unidad', to='planificaciones.Unidad')),
            ],
            options={
                'verbose_name_plural': 'planes de unidad',
                'db_table': 'planes_unidad',
            },
        ),
        migrations.CreateModel(
            name='PlanDestrezas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=50)),
                ('docentes', models.CharField(max_length=255)),
                ('paralelos', models.CharField(max_length=20)),
                ('aprobado_por', models.CharField(blank=True, max_length=50, null=True)),
                ('revisado_por', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('observaciones', models.TextField(blank=True, max_length=200, null=True)),
                ('ano_lectivo', models.CharField(max_length=9)),
                ('periodos', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31'), (32, '32'), (33, '33'), (34, '34'), (35, '35'), (36, '36'), (37, '37'), (38, '38'), (39, '39'), (40, '40')], default=1, validators=[django.core.validators.MaxValueValidator(40)])),
                ('semana_inicio', models.CharField(max_length=60)),
                ('ejes_transversales', models.TextField(max_length=255)),
                ('estrategias_metodologicas', models.TextField(max_length=700)),
                ('recursos', models.TextField(max_length=500)),
                ('actividades_evaluacion', models.TextField(max_length=600)),
                ('necesidad_adaptacion', models.TextField(blank=True, max_length=600, null=True)),
                ('adaptacion_curricular', models.TextField(blank=True, max_length=600, null=True)),
                ('asignatura', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='planes_destrezas', to='planificaciones.Asignatura')),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='planes_destrezas', to='planificaciones.Curso')),
                ('destrezas', models.ManyToManyField(related_name='planes_destrezas', to='planificaciones.Destreza')),
                ('elaborado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planes_destrezas', to=settings.AUTH_USER_MODEL)),
                ('objetivos', models.ManyToManyField(blank=True, related_name='planes_destrezas', to='planificaciones.Objetivo')),
                ('objetivos_generales', models.ManyToManyField(blank=True, related_name='planes_destrezas', to='planificaciones.ObjetivoGeneral')),
                ('unidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='planes_destrezas', to='planificaciones.Unidad')),
            ],
            options={
                'verbose_name_plural': 'planes de destrezas',
                'db_table': 'planes_destrezas',
            },
        ),
        migrations.CreateModel(
            name='PlanClase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=50)),
                ('docentes', models.CharField(max_length=255)),
                ('paralelos', models.CharField(max_length=20)),
                ('aprobado_por', models.CharField(blank=True, max_length=50, null=True)),
                ('revisado_por', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('observaciones', models.TextField(blank=True, max_length=200, null=True)),
                ('numero_plan', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('fecha', models.DateField()),
                ('numero_estudiantes', models.CharField(max_length=10)),
                ('tema', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(4)])),
                ('periodos', models.CharField(max_length=20)),
                ('metodologia', models.TextField(max_length=200, validators=[django.core.validators.MinLengthValidator(4)])),
                ('tecnica', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(4)])),
                ('bibliografia', ckeditor.fields.RichTextField()),
                ('contenido_cientifico', ckeditor_uploader.fields.RichTextUploadingField()),
                ('material_didactico', ckeditor_uploader.fields.RichTextUploadingField()),
                ('instrumento_evaluacion', ckeditor_uploader.fields.RichTextUploadingField()),
                ('asignatura', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='planes_clase', to='planificaciones.Asignatura')),
                ('cursos', models.ManyToManyField(related_name='planes_clase', to='planificaciones.Curso')),
                ('elaborado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planes_clase', to=settings.AUTH_USER_MODEL)),
                ('objetivos', models.ManyToManyField(blank=True, related_name='planes_clase', to='planificaciones.Objetivo')),
                ('objetivos_generales', models.ManyToManyField(blank=True, related_name='planes_clase', to='planificaciones.ObjetivoGeneral')),
            ],
            options={
                'verbose_name_plural': 'planes de clase',
                'db_table': 'planes_clase',
            },
        ),
        migrations.CreateModel(
            name='PlanAnual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=50)),
                ('docentes', models.CharField(max_length=255)),
                ('paralelos', models.CharField(max_length=20)),
                ('aprobado_por', models.CharField(blank=True, max_length=50, null=True)),
                ('revisado_por', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('observaciones', models.TextField(blank=True, max_length=200, null=True)),
                ('ano_lectivo', models.CharField(max_length=9)),
                ('carga_horaria', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31'), (32, '32'), (33, '33'), (34, '34'), (35, '35'), (36, '36'), (37, '37'), (38, '38'), (39, '39'), (40, '40')], default=1, validators=[django.core.validators.MaxValueValidator(40)])),
                ('semanas_trabajo', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31'), (32, '32'), (33, '33'), (34, '34'), (35, '35'), (36, '36'), (37, '37'), (38, '38'), (39, '39'), (40, '40')], default=1, validators=[django.core.validators.MaxValueValidator(40)])),
                ('semanas_imprevistos', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31'), (32, '32'), (33, '33'), (34, '34'), (35, '35'), (36, '36'), (37, '37'), (38, '38'), (39, '39'), (40, '40')], default=1, validators=[django.core.validators.MaxValueValidator(40)])),
                ('ejes_transversales', models.TextField(max_length=255)),
                ('bibliografia', ckeditor.fields.RichTextField()),
                ('asignatura', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='planes_anuales', to='planificaciones.Asignatura')),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='planes_anuales', to='planificaciones.Curso')),
                ('elaborado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planes_anuales', to=settings.AUTH_USER_MODEL)),
                ('objetivos_curso', models.ManyToManyField(blank=True, related_name='planes_anuales', to='planificaciones.Objetivo')),
                ('objetivos_generales', models.ManyToManyField(to='planificaciones.ObjetivoGeneral')),
                ('objetivos_generales_curso', models.ManyToManyField(blank=True, related_name='planes_anuales', to='planificaciones.ObjetivoGeneral')),
            ],
            options={
                'verbose_name_plural': 'planes anuales',
                'db_table': 'planes_anuales',
            },
        ),
        migrations.AddField(
            model_name='objetivo',
            name='subnivel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objetivos', to='planificaciones.Subnivel'),
        ),
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=700)),
                ('codigo', models.CharField(max_length=15)),
                ('criterio_evaluacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='indicadores', to='planificaciones.CriterioEvaluacion')),
            ],
            options={
                'verbose_name_plural': 'indicadores',
                'db_table': 'indicadores',
            },
        ),
        migrations.AddField(
            model_name='elementocurricular',
            name='plan_clase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elementos_curriculares', to='planificaciones.PlanClase'),
        ),
        migrations.AddField(
            model_name='destreza',
            name='subnivel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destrezas', to='planificaciones.Subnivel'),
        ),
        migrations.CreateModel(
            name='DesarrolloUnidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orientaciones_metodologicas', models.TextField(max_length=700)),
                ('semanas', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8')], default=1, validators=[django.core.validators.MaxValueValidator(8)])),
                ('destrezas', models.ManyToManyField(related_name='desarrollo_unidades', to='planificaciones.Destreza')),
                ('objetivos', models.ManyToManyField(blank=True, related_name='desarrollo_unidades', to='planificaciones.Objetivo')),
                ('objetivos_generales', models.ManyToManyField(blank=True, related_name='desarrollo_unidades', to='planificaciones.ObjetivoGeneral')),
                ('plan_anual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='desarrollo_unidades', to='planificaciones.PlanAnual')),
                ('unidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='desarrollo_unidades', to='planificaciones.Unidad')),
            ],
            options={
                'verbose_name_plural': 'desarrollo de unidades',
                'db_table': 'desarrollo_unidades',
            },
        ),
        migrations.AddField(
            model_name='curso',
            name='subnivel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursos', to='planificaciones.Subnivel'),
        ),
        migrations.AddField(
            model_name='criterioevaluacion',
            name='destrezas',
            field=models.ManyToManyField(related_name='criterios_evaluacion', to='planificaciones.Destreza'),
        ),
        migrations.AddField(
            model_name='criterioevaluacion',
            name='objetivos_generales',
            field=models.ManyToManyField(related_name='criterios_evaluacion', to='planificaciones.ObjetivoGeneral'),
        ),
        migrations.AddField(
            model_name='criterioevaluacion',
            name='subnivel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='criterios_evaluacion', to='planificaciones.Subnivel'),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='cursos',
            field=models.ManyToManyField(blank=True, related_name='asignaturas', to='planificaciones.Curso'),
        ),
        migrations.CreateModel(
            name='ActividadAprendizaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estrategias_metodologicas', models.TextField(max_length=600)),
                ('recursos', models.TextField(max_length=400)),
                ('instrumentos_evaluacion', models.TextField(max_length=600)),
                ('destrezas', models.ManyToManyField(related_name='actividades_aprendizaje', to='planificaciones.Destreza')),
                ('plan_unidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actividades_aprendizaje', to='planificaciones.PlanUnidad')),
            ],
            options={
                'verbose_name_plural': 'actividades de aprendizaje',
                'db_table': 'actividades_aprendizaje',
            },
        ),
    ]
