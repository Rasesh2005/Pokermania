# Generated by Django 4.2.18 on 2025-01-18 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poker', '0006_user_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='google_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile_picture',
        ),
    ]
