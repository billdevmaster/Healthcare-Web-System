# Generated by Django 2.0.5 on 2018-12-07 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0006_auto_20181207_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='patient_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='patient_phno',
        ),
    ]
