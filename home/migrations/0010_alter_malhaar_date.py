# Generated by Django 4.0.4 on 2022-05-31 13:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_malhaar_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='malhaar',
            name='date',
            field=models.DateTimeField(default=datetime.date(2022, 5, 31)),
        ),
    ]
