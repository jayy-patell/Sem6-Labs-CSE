from django.urls import path,include
from . import views

urlpatterns = [
        path('q1/',views.q1,name='q1'),
        path('newpage/',views.q1newpage,name='q1newpage'),
        path('q2/',views.q2,name='q2'),
        path('q2newpage/',views.q2newpage,name='q2newpage'),
    ]