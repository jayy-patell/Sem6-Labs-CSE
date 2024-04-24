from django.urls import path,include
from . import views

urlpatterns = [
        path('',views.geek_form_view,name='reg'),
        path('login_page',views.login_page,name='login_page'),
        # path('login',views.login,name='login'),
        path('login',views.login,name='login_session'),
        path('logout',views.logout,name='logout'),
    ]