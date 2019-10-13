from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    #path('create_listing/', views.save_listing, name='create_listing'),
    path('create_listing/', views.CreateListingView.as_view(success_url="/create_listing/"), name='create_listing'),
    path('lostandfound/', views.lafView, name='laf'),
    path('textbooks/', views.textbookView, name='textbook'),
    path('furniture', views.furniture, name='furniture'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)