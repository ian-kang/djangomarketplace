from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
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
        form = ListingForm(request.POST)
        if form.is_valid():
            new_listing = form.save()
            return redirect('/s/')
    else:
        form = ListingForm()
    return render(request, 'create_listing.html', {'form': form})

def itemlist(request):
    return render(request, "itemlist.html")

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
