from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views 

urlpatterns = [

    path('registro/', views.register_view, name='register'),
    

    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/inicio_sesion.html'
    ), name='login'),
    

    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]