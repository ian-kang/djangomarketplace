from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import datetime
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

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
            .replace(".", "")) # Unique id for each listing. Basically a big number. Feel free to fix
    category = models.CharField(max_length=15, choices=CATEGORIES)
    condition = models.CharField(max_length=25, choices=CONDITIONS)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=1000, blank=True)
    posted = models.DateTimeField(auto_now_add=True)
    images = models.FileField()
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, unique = True, null = False, db_index = True, on_delete=models.CASCADE)
    bio = models.TextField(max_length = 300, blank=True)
    location = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    #image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username

    def save(self):
        super().save()

#        img = Image.open(self.image.path)

#        if img.height > 300 or img.width > 300:
#            output_size = (300, 300)
#            img.thumbnail(output_size)
#            img.save(self.image.path)

@receiver(post_save, sender=User)
def create_user_profle(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Post(models.Model):
    user = models.TextField(max_length=200)
    title = models.TextField(max_length=200)
    description = models.TextField(max_length=1000)
    def __str__(self):
        return self.title
