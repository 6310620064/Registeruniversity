# Generated by Django 4.1.1 on 2022-09-14 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_rename_subjects_subject_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(max_length=50),
        ),
    ]
