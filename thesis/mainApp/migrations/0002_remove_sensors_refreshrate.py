# Generated by Django 2.2.7 on 2020-01-11 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensors',
            name='refreshRate',
        ),
    ]
