<<<<<<< HEAD
# Generated by Django 2.1.2 on 2018-11-17 19:28
=======
# Generated by Django 2.1.2 on 2018-11-17 21:53
>>>>>>> 3f1f9ce0b9c6bb10b082c5eaec6dbf835faf39d1

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=120)),
                ('password', models.CharField(max_length=20)),
                ('password1', models.CharField(max_length=20)),
            ],
        ),
    ]
