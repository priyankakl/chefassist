"""capstone2nd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from ChefAssist.views import *
from django.conf import settings      
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calendar/', calendar, name='calendar'),
    path('add_event/',add_event, name='add_event'),
    path('update',update, name='update'),
    path('remove/',remove, name='remove'),
    path('api/add_recipe/', add_recipe),
    path('api/recipes/', recipes),
    path('signup/',signup),
    path('signin/', signin),
    path('signout/', signout),
    path('recipe_list/',recipe_list),
    path('api/update_recipe/<str:title>/',update_recipe), 
    path('', home),   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

