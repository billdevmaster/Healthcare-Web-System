# Generated by Django 2.0.5 on 2018-11-23 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingPortalApp', '0001_initial'),
        ('rmp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rmpcontact',
            name='medicines',
            field=models.ManyToManyField(blank=True, to='shoppingPortalApp.medicine'),
        ),
    ]
