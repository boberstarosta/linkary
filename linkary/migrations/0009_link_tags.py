# Generated by Django 2.0.2 on 2018-02-12 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkary', '0008_auto_20180212_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='tags',
            field=models.ManyToManyField(blank=True, to='linkary.Tag'),
        ),
    ]
