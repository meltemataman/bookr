# Create your views here.
from django.http import HttpResponse
def welcome_view(request):
    return HttpResponse("Welcome to Bookrrrr!")

def hello_user(request):
    name = request.GET.get("name", "Guest")
    return HttpResponse(f"Hello, {name}!")
