from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Publisher

admin.site.register(Publisher)  # 👈 modeli admin panelde görünür yapar
