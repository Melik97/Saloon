# Generated by Django 4.1.7 on 2024-02-17 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
            ],
            options={
                'db_table': 'service',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SubService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('duration_minutes', models.IntegerField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.service')),
            ],
            options={
                'db_table': 'sub_service',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('customer_name', models.CharField(max_length=100)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.service')),
                ('sub_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.subservice')),
            ],
            options={
                'db_table': 'appointment',
                'ordering': ['-id'],
            },
        ),
    ]
