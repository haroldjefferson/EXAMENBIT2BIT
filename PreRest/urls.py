from unicodedata import name
from xml.etree.ElementInclude import include
from django.urls import path
from PreRest.views import RegistroUsuario

from . import views 
from django.contrib.auth import  views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('hacerpre', views.nuevapregunta),
    path('respuesta/<int:pk>/',views.respueston),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='registration/login.html'), name='logout'),
    path('registrar/', RegistroUsuario.as_view(), name='registrar')

]
