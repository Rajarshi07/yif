# Generated by Django 3.0.3 on 2021-01-08 00:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_files_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Files',
            new_name='File',
        ),
    ]