# Generated by Django 2.2.5 on 2019-10-31 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craigslist', '0005_listing_acct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='acct',
            field=models.CharField(max_length=20),
        ),
    ]