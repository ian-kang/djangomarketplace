from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.views.generic import FormView
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect

from .models import Listing
from .forms import ListingForm

# Create your views here.
def index(request):
    return render(request,"welcome.html")
    
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/s/')
    else:
        form = ListingForm()
    return render(request, 'create_listing.html', {'form': form})

def itemlist(request):
    return render(request, "itemlist.html")


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


class ItemList(generic.ListView):
    template_name = "itemlist.html"
    context_object_name = "itemlist"

    def get_queryset(self):
        return Listing.objects.all()


class LoginView(generic.TemplateView):
    template_name = "login.html"

class LogoutView(generic.TemplateView):
    template_name = "base.html"

def Logout(request):
    auth_logout(request)
    return redirect("base.html")

def redirect_view(request):
    response = redirect('/redirect-success/')
    return response
