# Generated by Django 2.2.6 on 2019-10-23 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wirecardbackend', '0014_remove_payment_boleto_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='boleto_number',
            field=models.IntegerField(null=True),
        ),
    ]