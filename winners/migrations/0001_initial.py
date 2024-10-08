# Generated by Django 5.1.1 on 2024-09-05 01:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('galleries', '0003_remove_gallery_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.PositiveIntegerField()),
                ('win_date', models.DateField()),
                ('weekly_like', models.PositiveIntegerField(default=0)),
                ('gallery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='galleries.gallery')),
            ],
        ),
    ]
