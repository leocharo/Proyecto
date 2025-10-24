from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class SimpleUserCreationForm(forms.ModelForm):
 
    email = forms.EmailField(required=True, label="Correo Electrónico") 
    username = forms.CharField(required=True, label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

    class Meta:
        model = User
        fields = ('email', 'username', 'password') 


    def save(self, commit=True):
        user = super().save(commit=False)
        
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user