# Generated by Django 2.2.6 on 2019-10-23 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wirecardbackend', '0008_payment_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='Payment_status',
            field=models.BooleanField(choices=[(0, 'Finalizado'), (1, 'Aguardando pagamento')]),
        ),
    ]
