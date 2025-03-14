from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm

# 🔹 User Registration View
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# 🔹 User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')

    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})



# # 🔹 Logout View (Redirect to Logged Out Page)
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    # return redirect('logged-out')
    return render(request, 'users/logout.html')

# 🔹 Logged Out Page View
# def logged_out_view(request):
#     return render(request, 'users/logout.html')

# 🔹 User Profile View (Requires Login)
@login_required
def profile(request):
    return render(request, 'users/profile.html')

