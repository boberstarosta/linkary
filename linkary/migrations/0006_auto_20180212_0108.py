# Generated by Django 2.0.2 on 2018-02-12 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linkary', '0005_auto_20180211_1828'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='link',
            options={'get_latest_by': ['time_created'], 'ordering': ['time_modified']},
        ),
    ]