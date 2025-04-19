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




