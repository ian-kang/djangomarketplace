from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import CreateListing

# Create your views here.
def index(request):
    return render(request,"base.html")

class CreateListingView(generic.ListView):
    template_name = 'create_listing.html'
    model = CreateListing
