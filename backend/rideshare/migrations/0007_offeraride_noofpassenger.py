# Generated by Django 4.0.6 on 2023-01-28 16:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0006_offeraride_delete_offerride'),
    ]

    operations = [
        migrations.AddField(
            model_name='offeraride',
            name='noOfPassenger',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
