# Generated by Django 4.0.4 on 2022-05-31 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_malhaar_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='totalVolume',
            field=models.IntegerField(default=0),
        ),
    ]