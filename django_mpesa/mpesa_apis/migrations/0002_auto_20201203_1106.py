# Generated by Django 3.0.4 on 2020-12-03 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa_apis', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transaction',
            new_name='LNMTransaction',
        ),
    ]