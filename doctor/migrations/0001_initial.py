<<<<<<< HEAD
# Generated by Django 2.0.5 on 2018-12-06 12:56
=======
# Generated by Django 2.0.5 on 2018-12-08 01:25
>>>>>>> 94edc6d85d5e3e18705ca09c3f9b87ecc786de7c

from django.db import migrations, models
import doctor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('slug', models.SlugField(default='abc')),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=40.5, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to=doctor.models.upload_image_path)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
