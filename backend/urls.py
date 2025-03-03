from django.urls import path
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from .views import (
    register_view,           
    profile_view, 
    travel_recommendations
    )

def home(request):
    return render(request, 'index.html')

urlpatterns = [
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='index.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    
    path('recommendations/', travel_recommendations, name='travel_recommendations'),
]
