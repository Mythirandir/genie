# Generated by Django 3.1.7 on 2021-05-02 15:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0009_auto_20210502_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 2, 16, 25, 10, 327238)),
        ),
    ]
