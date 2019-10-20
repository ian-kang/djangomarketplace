from django.contrib import admin

from .models import Listing
from .models import Profile

admin.site.register(Listing)
admin.site.register(Profile)