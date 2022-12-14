# Generated by Django 4.1.1 on 2022-09-13 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, unique=True)),
                ('subject_name', models.CharField(max_length=20)),
                ('semester', models.CharField(max_length=2)),
                ('academic_year', models.IntegerField()),
                ('quota', models.IntegerField()),
                ('status', models.BooleanField()),
                ('student', models.IntegerField(default=0)),
            ],
        ),
    ]
