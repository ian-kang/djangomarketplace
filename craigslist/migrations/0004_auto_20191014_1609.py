# Generated by Django 2.2.5 on 2019-10-14 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craigslist', '0003_auto_20191013_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='images',
            field=models.ImageField(upload_to='images/'),
        ),
    ]