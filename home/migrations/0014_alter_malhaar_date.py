# Generated by Django 4.0.4 on 2022-05-31 13:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_malhaar_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='malhaar',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
