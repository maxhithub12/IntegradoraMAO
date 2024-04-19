# Generated by Django 5.0.4 on 2024-04-19 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluacionServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio_id', models.PositiveIntegerField(null=True)),
                ('comentarios', models.TextField(null=True)),
                ('fecha_registro', models.DateField(null=True)),
                ('puntuacion', models.CharField(choices=[('Bueno', 'Bueno'), ('Regular', 'Regular'), ('Malo', 'Malo')], max_length=20, null=True)),
                ('persona_id', models.PositiveIntegerField(null=True)),
            ],
            options={
                'db_table': 'evaluacion_servicio',
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Abierta', 'Abierta'), ('Cerrada', 'Cerrada')], max_length=20, null=True)),
                ('persona_id', models.PositiveIntegerField(null=True)),
            ],
            options={
                'db_table': 'pregunta',
            },
        ),
        migrations.CreateModel(
            name='QuejaSugerencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.TextField()),
                ('estatus', models.CharField(choices=[('Pendiente', 'Pendiente'), ('En proceso', 'En proceso'), ('Resuelto', 'Resuelto')], max_length=20)),
                ('tipo', models.CharField(choices=[('Queja', 'Queja'), ('Sugerencia', 'Sugerencia')], max_length=20)),
                ('persona_id', models.PositiveIntegerField(null=True)),
            ],
            options={
                'db_table': 'quejas_sugerencias',
            },
        ),
        migrations.CreateModel(
            name='ServicioCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_servicio', models.CharField(max_length=50, null=True)),
                ('disponibilidad', models.CharField(choices=[('Disponible', 'Disponible'), ('No disponible', 'No disponible')], max_length=20, null=True)),
                ('descripcion', models.TextField()),
                ('instructor_id', models.PositiveIntegerField(null=True)),
                ('sucursal_id', models.PositiveIntegerField(null=True)),
            ],
            options={
                'db_table': 'servicio_al_cliente',
            },
        ),
        migrations.CreateModel(
            name='ServicioUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miembros_id', models.PositiveIntegerField(null=True)),
                ('servicio_id', models.PositiveIntegerField(null=True)),
                ('empleado_id', models.PositiveIntegerField(null=True)),
                ('fecha_de_uso', models.DateField(null=True)),
                ('tiempo_uso', models.TimeField(null=True)),
            ],
            options={
                'db_table': 'servicios_usuarios',
            },
        ),
        migrations.CreateModel(
            name='SucursalServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sucursal_id', models.PositiveIntegerField(null=True)),
                ('servicio_id', models.PositiveIntegerField(null=True)),
                ('estatus', models.CharField(choices=[('Disponible', 'Disponible'), ('No disponible', 'No disponible')], max_length=20, null=True)),
            ],
            options={
                'db_table': 'sucursales_servicios',
            },
        ),
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentarios', models.TextField(null=True)),
                ('fecha_registro', models.DateField(null=True)),
            ],
        ),
    ]