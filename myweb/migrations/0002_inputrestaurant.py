# Generated by Django 2.2.7 on 2020-10-25 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='inputrestaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('animename', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=1000)),
            ],
        ),
    ]
