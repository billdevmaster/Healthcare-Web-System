# Generated by Django 2.0.5 on 2018-11-27 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_profile', '0011_auto_20181126_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='date',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor_profile.BookingDate', unique=True),
        ),
        migrations.AlterField(
            model_name='slot',
            name='start_time',
            field=models.CharField(blank=True, choices=[('09:00:00', '6 am'), ('12:00:00', '12 pm'), ('04:00:00', '4 pm')], max_length=200, null=True, unique=True),
        ),
    ]
