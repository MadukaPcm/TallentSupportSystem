# Generated by Django 4.0 on 2022-01-13 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ADMINS', '0007_alter_media_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='description',
            field=models.TextField(max_length=2048),
        ),
    ]
