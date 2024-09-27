from django.urls import path
from .views import RegistroClienteView, ClienteLoginView, ActualizarPerfilView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.indexClientes, name='indexClientes'),  # Ruta de la vista indexClientes
    
    #Autentication
    path('register/', RegistroClienteView.as_view(template_name = "tienda/register.html"), name='register'),
    path('login/', ClienteLoginView.as_view(template_name = "tienda/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('perfil/', ActualizarPerfilView.as_view(template_name = "tienda/perfil_form.html"), name='perfil'),
]
