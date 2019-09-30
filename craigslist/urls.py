from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lostandfound/', views.lafView, name='laf'),
    path('textbooks/', views.textbookView, name='textbook'),
    path('furniture', views.furniture, name='furniture'),
]