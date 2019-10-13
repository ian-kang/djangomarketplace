from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.views.generic import FormView

from .models import CreateListing
from .forms import CreateListingForm

# Create your views here.
def index(request):
    return render(request,"base.html")

class CreateListingView(FormView):
    template_name = 'create_listing.html'
    form_class = CreateListingForm

    def save_listing(request):
        form = CreateListingForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            category = request.POST['category']
            condition = request.POST['category']
            price = request.POST['price']
            description = request.POST['description']
            images = request.POST['images']

            new_listing = CreateListing(title=title, category=category, condition=condition, price=price, description=description, images=images)
            new_listing.save()
        args = {'title':title, 'category':category, 'condition':condition, 'price':price, 'description':description, 'images':images}
        return render(request, 'create_listing.html',{'message': "Success! Your posting has been submitted!"}, args)



#    def form_valid(self, form):
#        return HttpResponse("Sweeeeeet.")
def lafView(request):
    return render(request, "lostandfound.html")
  
def textbookView(request):
    return render(request, "textbooks.html")

def furniture(request):
    return render(request,"furniture.html")

def login(request):
    return render(request,"login.html")
