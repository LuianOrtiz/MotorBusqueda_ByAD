# Generated by Django 4.0.5 on 2022-12-11 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Indice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=300)),
                ('analizado', models.BooleanField()),
                ('palabra_1', models.TextField(blank=True)),
                ('palabra_2', models.TextField(blank=True)),
                ('palabra_3', models.TextField(blank=True)),
            ],
        ),
    ]
