# Generated by Django 3.2.9 on 2021-12-01 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('AppointmentID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('AppointmentDate', models.DateField()),
                ('TimeSlot', models.CharField(default='09:00 PM - 10:00 PM', max_length=20)),
                ('AppointmentFee', models.FloatField(blank=True, default=0)),
                ('Remarks', models.CharField(blank=True, max_length=200, null=True)),
                ('Status', models.CharField(default='Pending', max_length=50)),
                ('Document', models.FileField(blank=True, null=True, upload_to='patients/appointment-documents/')),
                ('BookingTime', models.DateTimeField(auto_now_add=True, null=True)),
                ('DoctorUser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.docprofile')),
            ],
        ),
    ]
