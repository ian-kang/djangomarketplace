from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.views.generic import FormView
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect

from .models import Listing
from .forms import ListingForm, UserUpdateForm, ProfleUpdateForm, User, UserRegisterForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

class Profile(generic.TemplateView):
    template_name = "profile.html"

def Logout(request):
    auth_logout(request)
    return redirect("base.html")

def redirect_view(request):
    response = redirect('/redirect-success/')
    return response

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfleUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfleUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)