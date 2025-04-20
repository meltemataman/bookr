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
    name = request.GET.get('name', 'Ziyaretçi')
    book_count = request.GET.get('count', 0)
    context = {
        'user_name': name,
        'book_count': book_count
    }
    return render(request, 'personal_welcome.html', context)

def crash_view(request):
    # Force a ZeroDivisionError
    result = 1 / 0
    return HttpResponse(f"The result is {result}")

def debug_example_view(request):
    print("DEBUG: View çalışıyor...")
    value = "not_a_number"
    print(f"DEBUG: value = {value}")
    number = int(value)  # burada hata
    return HttpResponse(f"The number is {number}")




