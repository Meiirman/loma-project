# Generated by Django 4.1.2 on 2022-12-01 11:12

import colorfield.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0007_alter_lomauser_company'),
        ('couriers', '0004_alter_courier_company'),
        ('companies', '0003_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Новый этап', max_length=50)),
                ('color', colorfield.fields.ColorField(default='#2d4bf0', image_field=None, max_length=18, samples=None)),
                ('is_main_stage', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'stages',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Новый Продукт', max_length=50)),
                ('among', models.IntegerField(default=0)),
                ('price_per_piece', models.FloatField(default=0.0)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.company', verbose_name='Company')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=1000)),
                ('address', models.CharField(blank=True, default='', max_length=1000)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2022, 12, 1, 17, 12, 0, 898851))),
                ('change_date', models.DateTimeField(default=datetime.datetime(2022, 12, 1, 17, 12, 0, 898851))),
                ('budget', models.FloatField(blank=True, default=0.0)),
                ('delivery_date', models.DateTimeField(default=datetime.datetime(2022, 12, 1, 17, 12, 0, 898851))),
                ('message_sended', models.BooleanField(default=False)),
                ('source', models.CharField(blank=True, default='Создан вручную', max_length=250)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_%(model_name)s', to='companies.company', verbose_name='Company')),
                ('courier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsible_%(model_name)s', to='couriers.courier')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_%(model_name)s', to='users.lomauser')),
                ('product', models.ForeignKey(db_column='product', on_delete=django.db.models.deletion.CASCADE, to='orders.product')),
                ('responsible', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsible_%(model_name)s', to='users.lomauser')),
                ('stage', models.ForeignKey(db_column='stages', on_delete=django.db.models.deletion.CASCADE, to='orders.stage')),
            ],
        ),
    ]
