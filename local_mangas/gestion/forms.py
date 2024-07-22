from django import forms
from .models import Mangas, Libros, Comics, Figuras
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

#forms para crear el registro:
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#forms para edición de perfil de usuarios:
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Profile
        fields = ['image']

# Formulario combinado para actualizar perfil de usuario
class CustomUserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and len(password) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        return password


#Formulario para mangas:
class MangasForm(forms.ModelForm):
    class Meta:
        model = Mangas
        fields = ['nombre', 'tomo', 'editorial', 'autor', 'demografia', 'cantidad_stock', 'cantidad_hojas', 'precio', 'imagen']

#Formulario para libros:
class LibrosForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ['nombre', 'autor', 'editorial', 'genero', 'cantidad_stock', 'cantidad_hojas', 'precio', 'imagen']

#Formulario para cómics:
class ComicsForm(forms.ModelForm):
    class Meta:
        model = Comics
        fields = ['nombre', 'editorial', 'autor', 'genero', 'cantidad_stock', 'cantidad_hojas', 'precio', 'imagen']

#Formulario para las figuras:

class FigurasForm(forms.ModelForm):
    class Meta:
        model = Figuras
        fields = ['nombre','precio','cantidad_stock','imagen']