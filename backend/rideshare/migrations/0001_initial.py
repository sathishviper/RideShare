# Generated by Django 4.1.2 on 2022-10-10 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('uname', models.CharField(max_length=50)),
                ('email_id', models.EmailField(max_length=254, primary_key=True, serialize=False)),
            ],
        ),
    ]
