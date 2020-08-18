# Generated by Django 2.0.5 on 2020-08-07 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0006_remove_service_cus'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelapp.Customer')),
                ('Services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelapp.Service')),
            ],
            options={
                'db_table': 'custservice',
            },
        ),
    ]
