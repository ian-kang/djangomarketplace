from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"base.html")

def lafView(request):
    return render(request, "lostandfound.html")
  
def textbookView(request):
    return render(request, "textbooks.html")

def furniture(request):
    return render(request,"furniture.html")

def login(request):
    return render(request,"login.html")
