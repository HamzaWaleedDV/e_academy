# Generated by Django 4.2.5 on 2023-09-25 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('academy_courses', '0034_alter_orderproduct_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.TextField(verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy_courses.video', verbose_name='Video'),
        ),
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(max_length=5000, verbose_name='Course description'),
        ),
        migrations.AlterField(
            model_name='course',
            name='hour',
            field=models.IntegerField(verbose_name='Course hours'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Cover image'),
        ),
        migrations.AlterField(
            model_name='course',
            name='min',
            field=models.IntegerField(verbose_name='Course minutes'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Course title'),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.FloatField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='course',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='opinion',
            name='career',
            field=models.CharField(max_length=100, verbose_name='career'),
        ),
        migrations.AlterField(
            model_name='opinion',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Personal photo'),
        ),
        migrations.AlterField(
            model_name='opinion',
            name='message',
            field=models.TextField(max_length=500, verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='opinion',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='order',
            name='transaction',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='academy_courses.transaction', verbose_name='Transaction'),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='academy_courses.course', verbose_name='Course'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='academy_courses.order', verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='price',
            field=models.FloatField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Slider image'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='is_active',
            field=models.CharField(choices=[('', 'Select status'), ('active', 'Active'), (' ', 'Inactive')], default='Select status', max_length=50, verbose_name='Is active'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='academy_courses.course', verbose_name='Course'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Completed')], default=0, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='urls',
            name='icon',
            field=models.CharField(choices=[('', 'Select an icon'), ('fa-facebook', 'Facebook'), ('fa-twitter', 'Twitter'), ('fa-instagram', 'Instagram'), ('fa-linkedin', 'LinkedIn'), ('fa-youtube', 'YouTube'), ('fa-pinterest', 'Pinterest'), ('fa-tumblr', 'Tumblr'), ('fa-flickr', 'Flickr'), ('fa-github', 'GitHub'), ('fa-bitbucket', 'Bitbucket'), ('fa-gitlab', 'GitLab'), ('fa-stack-overflow', 'Stack Overflow'), ('fa-medium', 'Medium'), ('fa-reddit', 'Reddit'), ('fa-whatsapp', 'WhatsApp'), ('fa-skype', 'Skype')], default='Select an icon', max_length=100, verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='urls',
            name='title',
            field=models.CharField(default='My Urls', max_length=30, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='urls',
            name='url',
            field=models.URLField(verbose_name='Url'),
        ),
        migrations.AlterField(
            model_name='video',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy_courses.course', verbose_name='Course'),
        ),
        migrations.AlterField(
            model_name='video',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Video title'),
        ),
        migrations.AlterField(
            model_name='video',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='', verbose_name='Video'),
        ),
    ]
