# Generated by Django 4.0.4 on 2022-04-23 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carss', '0007_rename_car_photo_car_car_photo_1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='car_photo_1',
            new_name='car_photo',
        ),
    ]
