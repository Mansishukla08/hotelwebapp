# Generated by Django 2.0.5 on 2020-08-02 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0003_remove_booking_roomno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='staffid',
        ),
    ]