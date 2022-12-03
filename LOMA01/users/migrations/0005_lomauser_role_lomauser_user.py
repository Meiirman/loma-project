# Generated by Django 4.1.2 on 2022-10-29 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_alter_lomauser_options_remove_lomauser_last_login_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lomauser',
            name='role',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='users.role', verbose_name='Role'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lomauser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
