# Generated by Django 2.2.5 on 2019-11-10 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craigslist', '0003_auto_20191110_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='images',
        ),
        migrations.AlterField(
            model_name='listing',
            name='listing_id',
            field=models.CharField(default='20191110185403299912', max_length=50),
        ),
    ]
