from django.db import models

# Create your models here.

CONDITIONS = (
    ('NEW', 'New'),
    ('OPEN_BOX', 'Open Box'),
    ('USED', 'Used'),
    ('REFURBISHED', 'Refurbished'),
    ('FOR_PARTS', 'For Parts or Not Working'),
)

CATEGORIES = (
    ('FURNITURE', 'Furniture'),
    ('TEXTBOOKS', 'Textbooks'),
    ('HOUSING', 'Housing'),
    ('SERVICES', 'Services'),
    ('GIGS', 'Gigs'),
    ('LOST_AND_FOUND', 'Lost & Found'),
    ('OTHER', 'Other'),
)

class Listing(models.Model):

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=15, choices=CATEGORIES)
    condition = models.CharField(max_length=25, choices=CONDITIONS)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=1000, blank=True)
    posted = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title
