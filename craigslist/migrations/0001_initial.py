# Generated by Django 2.2.5 on 2019-12-02 01:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('acct', models.CharField(max_length=20)),
                ('listing_id', models.IntegerField(default='0000')),
                ('category', models.CharField(choices=[('FURNITURE', 'Furniture'), ('TEXTBOOKS', 'Textbooks'), ('HOUSING', 'Housing'), ('SERVICES', 'Services'), ('GIGS', 'Gigs'), ('LOST_AND_FOUND', 'Lost & Found'), ('OTHER', 'Other')], max_length=15)),
                ('condition', models.CharField(choices=[('NEW', 'New'), ('OPEN_BOX', 'Open Box'), ('USED', 'Used'), ('REFURBISHED', 'Refurbished'), ('FOR_PARTS', 'For Parts or Not Working')], max_length=25)),
                ('location', models.CharField(choices=[('ALDERMAN LIBRARY', 'Alderman Library'), ('CLARK LIBRARY', 'Clark Library'), ('CLEMONS LIBRARY', 'Clemons Library'), ('THORNTON HALL', 'Thornton Hall'), ('NEWCOMB HALL', 'Newcomb Hall'), ('OTHER', 'Other')], default='OTHER', max_length=25)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('posted', models.TimeField(auto_now_add=True)),
                ('images', models.FileField(upload_to='')),
                ('sold', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField(max_length=200)),
                ('title', models.TextField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=300)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
