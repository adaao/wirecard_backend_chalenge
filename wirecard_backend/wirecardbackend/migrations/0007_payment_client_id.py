# Generated by Django 2.2.6 on 2019-10-23 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wirecardbackend', '0006_auto_20191023_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='Client_id',
            field=models.ForeignKey(default=int, on_delete=django.db.models.deletion.CASCADE, to='wirecardbackend.Client'),
            preserve_default=False,
        ),
    ]
