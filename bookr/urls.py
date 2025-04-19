"""
URL configuration for bookr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from reviews.views import(
    home,
    welcome_template_view,
    personalized_welcome_view,
    query_example_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('template/', welcome_template_view),
    path('query/', query_example_view),
    path('', home),
    path('personal/', personalized_welcome_view),

]
