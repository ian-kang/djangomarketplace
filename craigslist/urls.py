from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    #path('create_listing/', views.CreateListingView.as_view(success_url="/create_listing/"), name='create_listing'),
    path('create_listing/', views.create_listing, name='create_listing'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('s/', views.ItemList.as_view(), name='itemlist'),
    path('<str:user>/<str:id>/', views.ListingView.as_view(), name='listing'), # Path for viewing other user listings. YYYYMMDDHH:MM:SS
    path('<str:user>/', views.ForeignProfileView.as_view(), name='profile'), # Path for viewing other user page
    path('profile/', views.ProfileView.as_view(), name='profile'), # Path for user login

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

