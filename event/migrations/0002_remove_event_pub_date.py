# Generated by Django 5.1.2 on 2024-11-07 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='pub_date',
        ),
    ]
