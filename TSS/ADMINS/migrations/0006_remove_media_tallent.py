# Generated by Django 4.0 on 2022-01-03 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ADMINS', '0005_alter_follower_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='Tallent',
        ),
    ]
