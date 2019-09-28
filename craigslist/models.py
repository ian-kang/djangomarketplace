from django.db import models

# Create your models here.

class CreateListing(models.Model):
    CONDITIONS = (
        ('NEW', 'New'),
        ('USED', 'Used'),
        ('REFURBISHED', 'Refurbished'),
        ('FOR_PARTS', 'For Parts or Not Working'),
        ('OPEN_BOX', 'Open Box'),
    )

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=25, choices=CONDITIONS)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text