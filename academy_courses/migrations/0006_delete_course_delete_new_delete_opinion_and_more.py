# Generated by Django 4.2.5 on 2023-09-08 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy_courses', '0005_alter_course_hours_alter_course_min'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='New',
        ),
        migrations.DeleteModel(
            name='Opinion',
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
    ]
