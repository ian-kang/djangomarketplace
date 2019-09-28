from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_listing/', views.CreateListingView.as_view(), name='create_listing')
]