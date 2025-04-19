# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def welcome_template_view(request):
    return render(request, 'welcome.html')

def query_example_view(request):
    name = request.GET.get('name', 'Visitor')  # Get the "name" parameter
    message = f"Hello, {name}! Django greets you 👋"
    return HttpResponse(message)

def home(request):
    return render(request, 'home.html')

def personalized_welcome_view(request):
    context = {
        'user_name': 'Meltem',
        'favorite_book': 'The Little Prince'
    }
    return render(request, 'personal_welcome.html', context)

def crash_view(request):
    # Force a ZeroDivisionError
    result = 1 / 0
    return HttpResponse(f"The result is {result}")

def debug_example_view(request):
    name = request.GET.get('name', 'Guest')
    print(f"DEBUG: name received from request = {name}")  # 👈 print for debugging

    upper_name = name.upper()
    print(f"DEBUG: uppercased name = {upper_name}")  # 👈 another debug line

    return HttpResponse(f"Hello, {upper_name}!")




