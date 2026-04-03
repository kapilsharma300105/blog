from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, userupdateform, profileupdateform
def register (request):
    form = UserCreationForm(request.POST)
    if  form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Account created for {username}!')   
    else:
        form = UserCreationForm()    
    return render(request, 'users/register.html', {'form': form})
def login_view(request):
    return render(request, 'users/login.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = userupdateform(request.POST, instance=request.user)
        p_form = profileupdateform(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = userupdateform(instance=request.user)
        p_form = profileupdateform(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
