# Generated by Django 4.1.2 on 2022-10-29 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_company'),
        ('couriers', '0003_courier_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courier',
            name='company',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='companies.company', verbose_name='Company'),
        ),
    ]