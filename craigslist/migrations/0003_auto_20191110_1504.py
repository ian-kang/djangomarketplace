# Generated by Django 2.2.5 on 2019-11-10 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craigslist', '0002_auto_20191110_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_id',
            field=models.CharField(default='20191110150407606100', max_length=50),
        ),
    ]
