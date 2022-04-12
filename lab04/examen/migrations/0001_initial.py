# Generated by Django 4.0.3 on 2022-04-05 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('partido_politico', models.CharField(max_length=200)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examen.region')),
            ],
        ),
    ]
