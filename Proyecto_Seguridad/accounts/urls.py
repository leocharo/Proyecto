from django.urls import path
from . import views # <-- Aquí sí importamos 'views' porque están en la misma carpeta
from django.contrib.auth import views as auth_views # Para Login/Logout

urlpatterns = [
    # 1. Ruta de REGISTRO: Llama a tu función de Python en views.py
    # URL: /registro/
    path('registro/', views.register_view, name='register'),
    
    # 2. Ruta de INICIO DE SESIÓN: Usa la clase LoginView de Django
    # URL: /login/
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/inicio_sesion.html'
    ), name='login'),
    
    # 3. Ruta de CERRAR SESIÓN: Usa la clase LogoutView de Django
    # URL: /logout/
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]