# Generated by Django 3.1.4 on 2021-11-13 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docprofile',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='docprofile',
            name='blood_type',
        ),
        migrations.RemoveField(
            model_name='docprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='docprofile',
            name='clinical_employment',
        ),
        migrations.RemoveField(
            model_name='docprofile',
            name='height',
        ),
        migrations.RemoveField(
            model_name='docprofile',
            name='photo_id',
        ),
        migrations.RemoveField(
            model_name='docprofile',
            name='right_to_sell',
        ),
        migrations.RemoveField(
            model_name='docprofile',
            name='state',
        ),
        migrations.RemoveField(
            model_name='docprofile',
            name='weight',
        ),
    ]
