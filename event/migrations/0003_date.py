# Generated by Django 5.1.2 on 2024-12-14 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_remove_event_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateField()),
            ],
        ),
    ]