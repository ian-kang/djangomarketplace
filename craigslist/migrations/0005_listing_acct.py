# Generated by Django 2.2.5 on 2019-10-30 18:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('craigslist', '0004_auto_20191026_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='acct',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
