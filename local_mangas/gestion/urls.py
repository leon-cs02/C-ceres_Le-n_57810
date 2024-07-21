from django.urls import path, include
from gestion.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .views import CustomLoginView, ProfileView, SignUpView
from .views import SearchResultsView


urlpatterns = [
    #pagina principal
    path('', index, name="index"),

    #Mangas:

    path('mangas/', MangasView.as_view(), name="mangas"),
    path('mangasCreate/', MangasCreate.as_view(), name="mangasCreate"),
    path('mangasUpdate/<int:pk>/', MangasUpdate.as_view(), name="mangasUpdate"),
    path('mangasDelete/<int:pk>/', MangasDelete.as_view(), name="mangasDelete"),

    #Libros:

    path('libros/', LibrosView.as_view(), name="libros"),
    path('librosCreate/', LibrosCreate.as_view(), name="librosCreate"),
    path('librosUpdate/<int:pk>/', LibrosUpdate.as_view(), name="librosUpdate"),
    path('librosDelete/<int:pk>/', LibrosDelete.as_view(), name="librosDelete"),

    #Comics:
    path('comics/', ComicsView.as_view(), name="comics"),
    path('comicsCreate/', ComicsCreate.as_view(), name="comicsCreate"),
    path('comicsUpdate/<int:pk>/', ComicsUpdate.as_view(), name="comicsUpdate"),
    path('comicsDelete/<int:pk>/', ComicsDelete.as_view(), name="comicsDelete"),

    #Figuras:
     path('figuras/', FigurasView.as_view(), name="figuras"),
    path('figurasCreate/', FigurasCreate.as_view(), name="figurasCreate"),
    path('figurasUpdate/<int:pk>/', FigurasUpdate.as_view(), name="figurasUpdate"),
    path('figurasDelete/<int:pk>/', FigurasDelete.as_view(), name="figurasDelete"),

    #Autentication:
    path('login/', auth_views.LoginView.as_view(template_name='gestion/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='gestion/logout.html'), name='logout'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(template_name='gestion/profile.html'), name='profile'),
    path('signup/', SignUpView.as_view(template_name='gestion/signup.html'), name='signup'),

    #Barra de búsqueda:

    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('mangas/search/', MangasSearchResultsView.as_view(), name='mangas_search'),
    path('libros/search/', LibrosSearchResultsView.as_view(), name='libros_search'),
    path('comics/search/', ComicsSearchResultsView.as_view(), name='comics_search'),
    path('figuras/search/', FigurasSearchResultsView.as_view(), name='figuras_search'),

    #Acerca de mi:

    path('acerca', acerca, name='acerca'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
