from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.http import JsonResponse


def home(request):
    """Homepage view"""
    return render(request, 'home.html')


def login_view(request):
    """Login view"""
    if request.user.is_authenticated:
        return redirect('main:home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('main:home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


def signup_view(request):
    """Signup view"""
    if request.user.is_authenticated:
        return redirect('main:home')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created successfully! Welcome, {user.username}!')
            return redirect('main:home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})


@login_required
def ask_view(request):
    """Ask page view - requires authentication"""
    return render(request, 'ask.html')


def products_view(request):
    """Products page view"""
    from .models import Product
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def logout_view(request):
    """Logout view"""
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('main:home')


def chat_webhook(request):
    """Handle chat messages and forward to webhook"""
    if request.method == 'POST':
        try:
            import json
            import requests
            
            # Get the message from the request
            data = json.loads(request.body)
            message = data.get('message', '')
            user = data.get('user', 'Anonymous')
            timestamp = data.get('timestamp', '')
            
            # TODO: Replace with your actual webhook URL
            webhook_url = 'YOUR_WEBHOOK_URL_HERE'
            
            # Prepare the payload for your webhook
            webhook_payload = {
                'message': message,
                'user': user,
                'timestamp': timestamp,
                'source': 'Abir_Product_with_n8n_AI'
            }
            
            # Send to webhook
            response = requests.post(webhook_url, json=webhook_payload, timeout=10)
            
            if response.status_code == 200:
                try:
                    webhook_response = response.json()
                    return JsonResponse({
                        'success': True,
                        'response': webhook_response.get('response', 'Thank you for your message. Our team will get back to you soon!')
                    })
                except:
                    return JsonResponse({
                        'success': True,
                        'response': 'Thank you for your message. Our team will get back to you soon!'
                    })
            else:
                return JsonResponse({
                    'success': False,
                    'response': 'Sorry, I\'m having trouble connecting right now. Please try again later.'
                })
                
        except Exception as e:
            return JsonResponse({
                'success': False,
                'response': 'Sorry, I\'m having trouble connecting right now. Please try again later.'
            })
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)
