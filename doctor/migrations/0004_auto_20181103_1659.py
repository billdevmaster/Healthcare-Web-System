# Generated by Django 2.1.2 on 2018-11-03 11:29

from django.db import migrations, models
import doctor.models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_auto_20181103_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=doctor.models.upload_image_path),
        ),
    ]
