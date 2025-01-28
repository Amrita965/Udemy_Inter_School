# Generated by Django 5.1.5 on 2025-01-28 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0001_initial'),
        ('Teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='courses',
            field=models.ManyToManyField(blank=True, null=True, related_name='teachers', to='Courses.course'),
        ),
    ]
