# Generated by Django 4.2.5 on 2023-09-30 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_profile_courses_alter_profile_profile_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='staticfiles/img/profile.jpg', null=True, upload_to='', verbose_name='Profile photo'),
        ),
    ]
