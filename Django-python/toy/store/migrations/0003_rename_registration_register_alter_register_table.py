# Generated by Django 5.1.6 on 2025-02-20 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_registration'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='registration',
            new_name='register',
        ),
        migrations.AlterModelTable(
            name='register',
            table='register',
        ),
    ]
