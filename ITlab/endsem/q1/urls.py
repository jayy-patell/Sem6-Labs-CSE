from django.urls import path
from . import views

urlpatterns = [
    path('first/', views.first, name='first'),
    path('add/', views.add, name='add'),
    path('second/',views.second,name='second'),
    path('delete/<name>/', views.delete, name='delete'),
]