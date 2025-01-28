# Generated by Django 5.1.5 on 2025-01-28 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0001_initial'),
        ('Students', '0002_student_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, null=True, related_name='students', to='Courses.course'),
        ),
    ]
