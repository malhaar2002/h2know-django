# Generated by Django 4.0.4 on 2022-05-31 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('fullName', models.CharField(max_length=40)),
                ('floorNo', models.IntegerField()),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
