# Generated by Django 3.1.4 on 2020-12-03 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa_apis', '0003_auto_20201203_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lnmtransaction',
            name='MerchantRequestID',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
