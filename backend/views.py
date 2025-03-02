from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from backend.core.models import CustomUser
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from backend.core.chatgpt_services import get_visa_recommendations, get_budget_recommendations


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            login(request, user)
            return redirect('home') 
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile_view(request):
    return render(request, 'utils/profile.html')


@login_required
def travel_recommendations(request):
    user = request.user
    visa_data = None
    budget_data = None

    visa_toggle = request.GET.get('visa', 'on')
    budget_toggle = request.GET.get('budget', 'on') 
    
    if visa_toggle == 'on' and user.passport_country:
        visa_data = get_visa_recommendations(user.passport_country.name)
    
    if budget_toggle == 'on':
        budget = request.GET.get('budget_value', 1000)  # Default budget
        budget_data = get_budget_recommendations(budget)
    
    context = {
        'visa_data': visa_data,
        'budget_data': budget_data,
    }
    return render(request, 'dashboard/recommendations.html', context)