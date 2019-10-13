from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_listing/', views.CreateListingView.as_view(success_url="/create_listing/"), name='create_listing'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('s/', views.itemlist, name='itemlist'),

]
