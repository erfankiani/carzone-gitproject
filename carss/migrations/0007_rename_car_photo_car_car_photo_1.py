# Generated by Django 4.0.4 on 2022-04-23 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carss', '0006_rename_car_photo_1_car_car_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='car_photo',
            new_name='car_photo_1',
        ),
    ]
