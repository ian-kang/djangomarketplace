# Generated by Django 2.2.5 on 2019-11-10 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craigslist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_id',
            field=models.CharField(default='20191110133219448385', max_length=50),
        ),
    ]