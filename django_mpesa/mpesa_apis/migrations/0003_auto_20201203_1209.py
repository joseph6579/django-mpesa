# Generated by Django 3.1.4 on 2020-12-03 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa_apis', '0002_auto_20201203_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lnmtransaction',
            name='MpesaReceiptNumber',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
