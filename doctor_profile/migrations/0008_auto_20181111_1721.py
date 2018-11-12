# Generated by Django 2.1.2 on 2018-11-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_profile', '0007_auto_20181103_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(upload_to='media_/profile_pic/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='speciality',
            field=models.CharField(choices=[('ORTHOPAEDIC', 'ORTHOPAEDIC'), ('GYNACEOLOGIST', 'GYNACEOLOGIST'), ('ONCOLOGIST', 'ONCOLOGIST'), ('NEUROLOGIST', 'NEUROLOGIST')], max_length=250),
        ),
    ]
