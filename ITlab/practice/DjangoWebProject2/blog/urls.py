from django.urls import path
from . import views

urlpatterns = [
        path('',views.index,name='index'),
        path('archive/',views.archive,name='archive'),
        path('createblog/',views.create_blog,name='create_blog'),
    ]