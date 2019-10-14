# Generated by Django 2.2.5 on 2019-09-30 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craigslist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createlisting',
            name='images',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='createlisting',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]