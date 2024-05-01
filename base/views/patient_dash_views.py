from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . .models import User, UserProfile, EconomicNumbers, Form

@login_required(login_url='home')
def user_dashboard(request):
    user = User.objects.get(id=request.user.id)   
    user_profile = UserProfile.objects.filter(user=user).last()
    economic_numbers = EconomicNumbers.objects.filter(user=user).last()
    context = {
        'user': user,
        'user_profile': user_profile,
        'economic_numbers': economic_numbers,
        user: 'user'
    }
    return render(request, 'base/user_dashboard.html', context)

@login_required(login_url='login')
def patient_profile(request):
    user = request.user
    user_profile = UserProfile.objects.filter(user=user).last()
    economic_numbers = EconomicNumbers.objects.filter(user=user).last()
    context = {
        'user': user,
        'user_profile': user_profile,
        'economic_numbers': economic_numbers,
    }

    return render(request, 'base/patient-section/patient_profile.html', context)

@login_required(login_url='login')
def patient_record(request):
    user = request.user
    forms = Form.objects.filter(user=user)
    context = {'forms': forms}
    return render(request, 'base/patient-section/patient_record.html', context)

@login_required(login_url='login')
def data_privacy(request):
    if request.method == 'POST':
        if request.POST.get('acceptTerms') == 'accept':
            return redirect('choose_form')
        elif request.POST.get('acceptTerms') == 'decline':
            return redirect('user_dashboard')
    return render(request, 'base/patient-section/data_privacy.html')