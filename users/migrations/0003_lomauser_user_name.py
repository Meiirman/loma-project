# Generated by Django 4.1.2 on 2022-10-29 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_lomauser'),
    ]

    operations = [
        migrations.AddField(
            model_name='lomauser',
            name='user_name',
            field=models.CharField(default='User', max_length=50, unique=True, verbose_name='Name'),
        ),
    ]
