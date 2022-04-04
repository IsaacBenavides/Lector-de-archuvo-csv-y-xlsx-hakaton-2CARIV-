# Generated by Django 4.0.3 on 2022-04-02 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Uploader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='media/files')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Xlsx',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('item_type', models.CharField(max_length=255)),
                ('sales_channel', models.CharField(max_length=255)),
                ('order_priority', models.CharField(max_length=255)),
                ('order_date', models.DateField()),
                ('order_id', models.IntegerField()),
                ('ship_date', models.DateField()),
                ('units_sold', models.IntegerField()),
                ('unit_price', models.FloatField()),
                ('unit_cost', models.FloatField()),
                ('total_revenue', models.FloatField()),
                ('total_cost', models.FloatField()),
                ('total_profit', models.FloatField()),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reader.uploader')),
            ],
        ),
        migrations.CreateModel(
            name='CsvModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('deposits', models.DecimalField(decimal_places=2, max_digits=30)),
                ('withdrawls', models.DecimalField(decimal_places=2, max_digits=30)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=30)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reader.uploader')),
            ],
        ),
    ]
