from django.urls import path
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from .views import (
    register_view,           
    profile_view, 
    profile_update,
    search_view,
    destination_detail,
    )
from .api.search_api import (
    country_search_api, 
    currency_search_api,
    )

def home(request):
    return render(request, 'index.html')

urlpatterns = [
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='index.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('profile/update/', profile_update, name='profile_update'),
    
    path('api/country-search/', country_search_api, name='country_search_api'),
    path('api/currency-search/', currency_search_api, name='currency_search_api'),
    
    path("ajax-search/", search_view, name="ajax_search"),
    path("destination/<slug:slug>/", destination_detail, name="destination_detail")
]
