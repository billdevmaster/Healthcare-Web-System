# Generated by Django 2.1.2 on 2018-11-12 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingPortalApp', '0007_auto_20181112_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
