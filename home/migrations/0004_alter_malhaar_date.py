# Generated by Django 4.0.4 on 2022-05-31 13:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_malhaar_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='malhaar',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]