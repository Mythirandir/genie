# Generated by Django 3.1.7 on 2021-04-27 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_creator',
            field=models.ForeignKey(default='User', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
