# Proyecto_Seguridad/Proyecto_Seguridad/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView # <-- Importar RedirectView

urlpatterns = [
    # 1. Redirección de la Raíz (/) a la URL con nombre 'login'
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    
    # 2. Ruta de la administración de Django
    path('admin/', admin.site.urls),
    
    # 3. Incluye las URLs de la aplicación 'accounts' (sin prefijo)
    path('', include('accounts.urls')), 
    
]