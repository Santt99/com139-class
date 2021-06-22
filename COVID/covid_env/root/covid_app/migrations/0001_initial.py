# Generated by Django 3.2.3 on 2021-05-20 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='COVIDData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_registro', models.CharField(max_length=100)),
                ('origen', models.CharField(max_length=30)),
                ('sector', models.CharField(max_length=30)),
                ('entidad_um', models.CharField(max_length=2)),
                ('sexo', models.CharField(max_length=10)),
                ('entidad_nac', models.CharField(max_length=2)),
                ('entidad_res', models.CharField(max_length=2)),
                ('municipio_res', models.CharField(max_length=30)),
                ('tipo_paciente', models.CharField(max_length=30)),
                ('fecha_ingreso', models.DateField(blank=True, null=True)),
                ('fecha_sintomas', models.DateField(blank=True, null=True)),
                ('fecha_def', models.DateField(blank=True, null=True)),
                ('intubado', models.CharField(max_length=30)),
                ('neumonia', models.CharField(max_length=30)),
                ('edad', models.IntegerField(default=0)),
                ('nacionalidad', models.CharField(max_length=30)),
                ('embarazo', models.CharField(max_length=30)),
                ('habla_lengua_indig', models.CharField(max_length=30)),
                ('indigena', models.CharField(max_length=30)),
                ('diabetes', models.CharField(max_length=30)),
                ('epoc', models.CharField(max_length=30)),
                ('asma', models.CharField(max_length=30)),
                ('inmusupr', models.CharField(max_length=30)),
                ('hipertension', models.CharField(max_length=30)),
                ('otra_com', models.CharField(max_length=30)),
                ('cardiovascular', models.CharField(max_length=30)),
                ('obesidad', models.CharField(max_length=30)),
                ('renal_cronica', models.CharField(max_length=30)),
                ('tabaquismo', models.CharField(max_length=30)),
                ('otro_caso', models.CharField(max_length=30)),
                ('toma_muestra_lab', models.CharField(max_length=2)),
                ('resultado_lab', models.CharField(max_length=30)),
                ('toma_muestra_antigeno', models.CharField(max_length=30)),
                ('resultado_antigeno', models.CharField(max_length=30)),
                ('clasificacion_final', models.CharField(max_length=30)),
                ('migrante', models.CharField(max_length=30)),
                ('pais_nacionalidad', models.CharField(max_length=30)),
                ('pais_origen', models.CharField(max_length=30)),
                ('uci', models.CharField(max_length=30)),
                ('fecha_ingreso_yr', models.IntegerField(default=0)),
                ('fecha_ingreso_mt', models.IntegerField(default=0)),
                ('fecha_ingreso_dy', models.IntegerField(default=0)),
                ('fecha_ingreso_wk', models.IntegerField(default=0)),
                ('fecha_sintomas_yr', models.IntegerField(default=0)),
                ('fecha_sintomas_mt', models.IntegerField(default=0)),
                ('fecha_sintomas_dy', models.IntegerField(default=0)),
                ('fecha_sintomas_wk', models.IntegerField(default=0)),
                ('fecha_def_yr', models.IntegerField(blank=True, default=None, null=True)),
                ('fecha_def_mt', models.IntegerField(blank=True, default=None, null=True)),
                ('fecha_def_dy', models.IntegerField(blank=True, default=None, null=True)),
                ('fecha_def_wk', models.IntegerField(blank=True, default=None, null=True)),
            ],
            options={
                'db_table': 'covid_data',
            },
        ),
    ]