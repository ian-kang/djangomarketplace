from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"base.html")

def furniture(request):
    return render(request,"furniture.html")