# Generated by Django 2.0.2 on 2018-02-10 13:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('linkary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 2, 10, 13, 14, 37, 442008, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='link',
            name='time_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
