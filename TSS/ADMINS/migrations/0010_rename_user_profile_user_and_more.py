# Generated by Django 4.0 on 2022-01-16 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ADMINS', '0009_follower_user_media_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='User',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='userdetails',
            old_name='User',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='follower',
            name='UserDetails',
        ),
        migrations.RemoveField(
            model_name='media',
            name='UserDetails',
        ),
    ]
