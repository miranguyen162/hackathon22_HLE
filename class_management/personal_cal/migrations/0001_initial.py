# Generated by Django 4.1 on 2022-09-17 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='time_table',
            fields=[
                ('stt', models.AutoField(primary_key=True, serialize=False)),
                ('hp', models.CharField(blank=True, max_length=255, null=True)),
                ('si_so', models.IntegerField()),
                ('buoi', models.CharField(blank=True, max_length=10, null=True)),
                ('thu', models.IntegerField()),
                ('giang_duong', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('stt', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=20, null=True)),
                ('category', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
