# Generated by Django 5.1.5 on 2025-01-30 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0003_student_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='photo',
        ),
    ]
