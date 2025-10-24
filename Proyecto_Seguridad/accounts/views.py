from django.shortcuts import render, redirect
from .forms import SimpleUserCreationForm # <-- ¡CORREGIDO!
from django.contrib.auth.decorators import login_required

@login_required # Asegura que solo usuarios logueados puedan ver esta página
def dashboard_view(request):
    # Renderiza la nueva plantilla
    return render(request, 'accounts/dashboard.html')

def register_view(request):
    if request.method == 'POST':
        form = SimpleUserCreationForm(request.POST) # Usar el formulario simple
        
        if form.is_valid():
            # El método .save() ahora cifra la contraseña
            user = form.save() 
            return redirect('login')
            
    else:
        form = SimpleUserCreationForm() # Usar el formulario simple
        
    # Renderiza la plantilla, pasando el formulario
    return render(request, 'accounts/registro.html', {'form': form})