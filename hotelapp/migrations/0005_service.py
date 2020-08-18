# Generated by Django 2.0.5 on 2020-08-02 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0004_remove_booking_staffid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('tariff', models.FloatField()),
                ('description', models.CharField(max_length=200)),
                ('Cus', models.ManyToManyField(to='hotelapp.Customer')),
            ],
            options={
                'db_table': 'service',
            },
        ),
    ]