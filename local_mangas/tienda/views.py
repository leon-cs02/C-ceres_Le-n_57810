from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import CreateView
from .forms import RegistroClienteForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from .models import PerfilCliente


#Redirection
def indexClientes(request):
    return render(request, 'tienda/indexClientes.html')

#------------------------------------------------------------------------------------------------------------------------
#Autentication for clients

class RegistroClienteView(CreateView):
    form_class = RegistroClienteForm
    template_name = 'register.html'
    success_url = reverse_lazy('indexClientes')  # Redirigir después del registro

    def form_valid(self, form):
        # Guardar el usuario y hacer login automáticamente
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class ClienteLoginView(LoginView):
    template_name = 'login.html'



class ActualizarPerfilView(LoginRequiredMixin, UpdateView):
    model = PerfilCliente
    fields = ['telefono', 'direccion']
    template_name = 'perfil_form.html'
    success_url = reverse_lazy('perfil')

    def get_object(self, queryset=None):
        # Retorna el perfil del usuario autenticado
        return self.request.user.perfilcliente


#------------------------------------------------------------------------------------------------------------------------