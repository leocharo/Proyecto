from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class SimpleUserCreationForm(forms.ModelForm):
    # Definimos explícitamente los campos que queremos:
    email = forms.EmailField(required=True, label="Correo Electrónico") 
    username = forms.CharField(required=True, label="Usuario")
    # Usamos PasswordInput para asegurar que el campo se muestre oculto
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

    class Meta:
        model = User
        fields = ('email', 'username', 'password') # Solo estos campos

    # Método crucial para guardar la contraseña de forma CIFRADA
    def save(self, commit=True):
        user = super().save(commit=False)
        # ESTA LÍNEA ES LA QUE CIFRA LA CONTRASEÑA antes de guardarla
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user