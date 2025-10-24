# Proyecto_Seguridad/Proyecto_Seguridad/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView 

urlpatterns = [
  
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    
 
    path('admin/', admin.site.urls),
    
    
    path('', include('accounts.urls')), 
    
]