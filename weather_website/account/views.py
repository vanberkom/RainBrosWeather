from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Account
from weatherUpdate.views import index
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        print('post')
        # Get form data
        username = request.POST.get('username')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        notifications = request.POST.get('notifications') == 'on'  # Checkbox value
        phone_number = request.POST.get('phone_number')

        # Check for missing data
        if not username or not password or not first_name or not last_name:
            print('username',username)
            messages.error(request, 'Please provide all required fields.')
            return render(request, 'register.html')

        # Validate password confirmation
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')

        try:
            # Create the user
            user = User.objects.create_user(username=username, password=password)
            user.first_name = first_name  # Set first name in User
            user.last_name = last_name    # Set last name in User
            user.save()

            # Create the Account instance and associate it with the user
            account = Account(
                user=user,
                first_name=first_name,
                last_name=last_name,
                notifications=notifications,
                phone_number=phone_number
            )
            account.save()

            # Authenticate and log in the user
            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                
                return render(request, 'index.html')
        except Exception as e:
            # Handle exceptions, such as user already existing
            messages.error(request, f'Error creating user or account: {e}')
        
        # Render the registration form again on error
        return render(request, 'register.html')

    # If not POST, render the registration form
    return render(request, 'register.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['user_name'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect('index')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 

    form = AuthenticationForm() 
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('index')