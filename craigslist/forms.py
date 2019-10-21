from django import forms
from .models import Listing
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

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

class ListingForm(forms.ModelForm):

    category = forms.ChoiceField(choices=CATEGORIES, required=True )
    condition = forms.ChoiceField(choices=CONDITIONS, required=True )
    images = forms.ImageField()

    #title = forms.TextInput(attrs={'placeholder': ' What are you selling? '})
    #price = forms.NumberInput(attrs={'placeholder': 'How much do you want? '})
    #description = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20, 'placeholder': ' Provide details '})),
    #need timestamp

    class Meta:
        title = forms.TextInput()
        model = Listing
        fields = ['title', 'price', 'description', 'images', 'category', 'condition',]

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': ' What are you selling? '}),
            'price': forms.NumberInput(attrs={'placeholder': 'How much do you want? ', 'style':'width:23ch'}),
            'description': forms.Textarea(attrs={'placeholder': ' Provide details '}),
        #    'images': forms.ImageField(),
        #    #need timestamp
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfleUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image']

