# Generated by Django 4.1.2 on 2022-10-29 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_lomauser_user_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lomauser',
            options={},
        ),
        migrations.RemoveField(
            model_name='lomauser',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='lomauser',
            name='password',
        ),
        migrations.RemoveField(
            model_name='lomauser',
            name='role',
        ),
        migrations.RemoveField(
            model_name='lomauser',
            name='user_name',
        ),
        migrations.AlterModelTable(
            name='lomauser',
            table=None,
        ),
    ]