# Generated by Django 5.1.3 on 2025-03-11 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_customuser_friends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='friends',
        ),
    ]
