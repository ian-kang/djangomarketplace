from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import datetime

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
    acct = models.CharField(max_length=20) # Hidden field to keep track of who posted what
    listing_id = models.CharField(max_length=50, 
        default=str(datetime.now())
            .replace("-", "")
            .replace(" ", "")
            .replace(":", "")
            .replace(".", "")) # Unique id for each listing. Basically a big ass number. Formatting is shit, feel free to fix
    category = models.CharField(max_length=15, choices=CATEGORIES)
    condition = models.CharField(max_length=25, choices=CONDITIONS)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=1000, blank=True)
    posted = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)