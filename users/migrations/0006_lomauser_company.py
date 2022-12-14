# Generated by Django 4.1.2 on 2022-10-29 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_company'),
        ('users', '0005_lomauser_role_lomauser_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='lomauser',
            name='company',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to='companies.company', verbose_name='Company'),
            preserve_default=True,
        ),
    ]
