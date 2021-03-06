# Generated by Django 3.2.9 on 2021-12-01 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user', unique=True)),
                ('ProfilePicture', models.ImageField(default='patients/profile_images/profile-default.png', null=True, upload_to='patients/profile_pictures/')),
                ('FirstName', models.CharField(max_length=65)),
                ('LastName', models.CharField(max_length=65)),
                ('Address', models.CharField(max_length=200)),
                ('PhoneNumber', models.CharField(max_length=200)),
                ('DOB', models.DateField(null=True)),
                ('BloodGroup', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('ReportID', models.CharField(default='0', max_length=20, primary_key=True, serialize=False)),
                ('DiagnosisName', models.CharField(max_length=100, null=True)),
                ('Document', models.FileField(null=True, upload_to='patients/medical-history/')),
                ('PatientUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.patients')),
            ],
        ),
    ]
