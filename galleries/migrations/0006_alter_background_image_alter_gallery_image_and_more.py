# Generated by Django 5.1.1 on 2024-09-06 08:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0005_alter_category_name_alter_gallery_like_users_and_more'),
        ('users', '0003_alter_user_profile_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='background',
            name='image',
            field=models.ImageField(upload_to='backgrounds/%Y/%m/%d/7f47291e-9728-4cce-b443-b8c3951c900f/'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='galleries/%Y/%m/%d/b2407068-7709-4196-bd2a-0bf4bfd0fa84/'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='like_users',
            field=models.ManyToManyField(related_name='liking_galleries', through='users.UserGallery', to=settings.AUTH_USER_MODEL),
        ),
    ]
