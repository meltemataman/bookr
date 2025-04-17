from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def welcome_view(request):
    return HttpResponse("Welcome to Bookr!")

def query_view(request):
    value = request.GET.get('q', 'No query')
    return HttpResponse(f"Query value: {value}")

from django.shortcuts import render

def welcome_view(request):
    return render(request, "welcome.html")
