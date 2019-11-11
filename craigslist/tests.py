import pytz
import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Listing

class ListingModelTests(TestCase):
    def test_listing_was_posted_recently_with_new_question(self):
        l1 = Listing()
        l1.save()
        self.assertIs(l1.posted_recently(), True)

    def test_listing_was_posted_recently_with_old_question(self):
        time = timezone.now() + datetime.timedelta(days=10)
        l1 = Listing()
        l1.save()
        l1.posted = time
        self.assertIs(l1.posted_recently(), False)
