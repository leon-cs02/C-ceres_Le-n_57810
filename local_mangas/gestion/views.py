from django.shortcuts import render
from gestion.models import *
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.views import LoginView
from .forms import CustomUserProfileForm, ProfileUpdateForm
from django.contrib.auth.models import User
from .models import Profile
from gestion.forms import *
from django.contrib.auth.decorators import login_required
from .models import Mangas, Libros, Comics
from django.conf import settings

# Métodos para visualizar en la página los html

#Función para poder ver el index.html
def index(request):
    mangas = Mangas.objects.all()[:4]  # Traer los primeros 4 mangas
    libros = Libros.objects.all()[:4]  # Traer los primeros 4 libros
    comics = Comics.objects.all()[:4]  # Traer los primeros 4 cómics
    figuras =  Figuras.objects.all()[:4]
    context = {
        'mangas': mangas,
        'libros': libros,
        'comics': comics,
        'figuras': figuras,
        'MEDIA_URL': settings.MEDIA_URL,  # Agregar MEDIA_URL al contexto
    }
    return render(request, 'gestion/index.html', context)

#------------------------------------------------------------------------------------------------------------

#Utilizo CBV para modificar el perfil de usuario, validar los métodos get y post, guardar los datos y finalizar
#con un mensaje que indique que su perfil fue modificado:

class CustomLoginView(LoginView):
    template_name = 'login.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        return self.render_to_response({'u_form': u_form, 'p_form': p_form})

    def post(self, request, *args, **kwargs):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Se guardaron los datos con éxito!')
            return redirect('profile')

        return self.render_to_response({'u_form': u_form, 'p_form': p_form})
    
#------------------------------------------------------------------------------------------------------------

#Registro:

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')  # Redirige a la página de login después de registrarse
    template_name = 'signup.html'

#------------------------------------------------------------------------------------------------------------

#Métodos pertenecientes a los Mangas:


#Ver mangas:
class MangasView(ListView, LoginRequiredMixin):
    model = Mangas

#Subir mangas a la BD:
class MangasCreate(CreateView, LoginRequiredMixin):
    model = Mangas
    fields = ["nombre","tomo","editorial","autor","demografia","cantidad_stock","cantidad_hojas","precio", "imagen"]
    success_url = reverse_lazy("mangas")

#Actualizar los datos de la BD de los mangas:
class MangasUpdate(UpdateView, LoginRequiredMixin):
    model = Mangas
    fields = ["nombre","tomo","editorial","autor","demografia","cantidad_stock","cantidad_hojas","precio", "imagen"]
    success_url = reverse_lazy("mangas")

#Borrar datos en la BD:
class MangasDelete(DeleteView, LoginRequiredMixin):
    model = Mangas
    success_url = reverse_lazy("mangas")

#Filtro:

class MangasSearchResultsView(ListView):
    model = Mangas
    template_name = 'gestion/mangas_search_results.html'
    context_object_name = 'mangas_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        tomo = self.request.GET.get('tomo')
        if tomo:
            return Mangas.objects.filter(nombre__icontains=query, tomo=tomo)
        return Mangas.objects.filter(nombre__icontains=query)

#------------------------------------------------------------------------------------------------------------

#Métodos pertenecientes al Model Cómics:

#Ver Cómics:
class ComicsView(ListView, LoginRequiredMixin):
    model = Comics

#Subir cómics a la BD:
class ComicsCreate(CreateView, LoginRequiredMixin):
    model = Comics
    fields = ["nombre","editorial","autor","genero","cantidad_stock","cantidad_hojas","precio", "imagen"]
    success_url = reverse_lazy("comics")

#Actualizar los datos de la BD de los Cómics:
class ComicsUpdate(UpdateView, LoginRequiredMixin):
    model = Comics
    fields = ["nombre","editorial","autor","genero","cantidad_stock","cantidad_hojas","precio", "imagen"]
    success_url = reverse_lazy("comics")

#Borrar datos en la BD:
class ComicsDelete(DeleteView, LoginRequiredMixin):
    model = Comics
    success_url = reverse_lazy("comics")

#Filtro:

class ComicsSearchResultsView(ListView):
    model = Comics
    template_name = 'gestion/comics_search_results.html'
    context_object_name = 'comics_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Comics.objects.filter(nombre__icontains=query)

#------------------------------------------------------------------------------------------------------------

#Métodos pertenecientes al model Libros:

#Ver libros:
class LibrosView(ListView, LoginRequiredMixin):
    model = Libros

#Método para agregar a la BD:
class LibrosCreate(CreateView, LoginRequiredMixin):
    model = Libros
    fields = ["nombre","editorial","autor","genero","cantidad_stock","cantidad_hojas","precio", "imagen"]
    success_url = reverse_lazy("libros")

#Método para actualizar los campos de los libros:
class LibrosUpdate(UpdateView, LoginRequiredMixin):
    model = Libros
    fields = ["nombre","editorial","autor","genero","cantidad_stock","cantidad_hojas","precio", "imagen"]
    success_url = reverse_lazy("libros")

#Método para borrar de la BD un libro:
class LibrosDelete(DeleteView, LoginRequiredMixin):
    model = Libros
    success_url = reverse_lazy("libros")

#Filtro:

class LibrosSearchResultsView(ListView):
    model = Libros
    template_name = 'gestion/libros_search_results.html'
    context_object_name = 'libros_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Libros.objects.filter(nombre__icontains=query)


#------------------------------------------------------------------------------------------------------------

#Ver figuras:
class FigurasView(ListView, LoginRequiredMixin):
    model = Figuras

#Agregar Figuras a la BD:
class FigurasCreate(CreateView, LoginRequiredMixin):
    model = Figuras
    fields = ["nombre", "precio", "imagen"]
    success_url = reverse_lazy("figuras")

#Actualizar los campos:
class FigurasUpdate(UpdateView, LoginRequiredMixin):
    model = Figuras
    fields = ["nombre", "precio", "imagen"]
    success_url = reverse_lazy("figuras")

#Eliminar los datos:
class FigurasDelete(DeleteView, LoginRequiredMixin):
    model = Figuras
    success_url = reverse_lazy("figuras")

#Filtro:

class FigurasSearchResultsView(ListView):
    model = Figuras
    template_name = 'gestion/figuras_search_results.html'
    context_object_name = 'figuras_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Figuras.objects.filter(nombre__icontains=query)

#------------------------------------------------------------------------------------------------------------

#Barra de búsqueda: 

class SearchResultsView(ListView):
    template_name = 'gestion/search_results.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = {
            'mangas': Mangas.objects.filter(nombre__icontains=query),
            'libros': Libros.objects.filter(nombre__icontains=query),
            'comics': Comics.objects.filter(nombre__icontains=query),
            'figuras': Figuras.objects.filter(nombre__icontains=query)
        }
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_queryset())
        context['query'] = self.request.GET.get('q')
        return context
#------------------------------------------------------------------------------------------------------------

#Apartado de "Acerca De"
def acerca(request):
    return render(request, 'gestion/acercaDeMi.html')