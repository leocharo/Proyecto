from django.shortcuts import render, redirect
from .forms import SimpleUserCreationForm 
from django.contrib.auth.decorators import login_required

@login_required 
def dashboard_view(request):
    
    return render(request, 'accounts/dashboard.html')

def register_view(request):
    if request.method == 'POST':
        form = SimpleUserCreationForm(request.POST) 
        
        if form.is_valid():
           
            user = form.save() 
            return redirect('login')
            
    else:
        form = SimpleUserCreationForm() 
        

    return render(request, 'accounts/registro.html', {'form': form})