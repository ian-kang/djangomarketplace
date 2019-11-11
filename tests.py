from django.urls import resolve
from django.test import TestCase
from django.contrib.auth.models import User
from craigslist.forms import ListingForm
from craigslist.models import Listing
from craigslist.views import index, create_listing, LogoutView, ItemList, LocationView, ForeignProfileView

class ViewTests(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, index) 
    def test_create_listing_url_resolves_to_create_listing_view(self):
        found = resolve('/create_listing/')  
        self.assertEqual(found.func, create_listing) 
    def setUp(self):
        self.user = User.objects.create_superuser(
            'admin',
            'admin@admin.com',
            'password'
        )
    def test_create_listing(self): 
        self.client.login(username='admin', password='password')
        form_data = { 
            'title': 'car',
            'price': 42000,
            'description': ('this is a car'),
            'images': '',
            'category': ('FURNITURE', 'Furniture'),
            'condition': ('NEW', 'New'),
            'acct': 'admin'
        } 
        form = ListingForm(data=form_data)
        response = self.client.post('create_listing/', form_data)
        num_of_listings = Listing.objects.all().count()
        temp = Listing.objects.get(title=form_data['title'])
        self.assertTrue(form.is_valid())
        self.assertEqual(temp.author, self.user1)
        self.assertEqual(num_of_listings, 1)
        
def foo():
    return True

def test():
    assert foo() == True