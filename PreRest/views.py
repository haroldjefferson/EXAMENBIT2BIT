from django.shortcuts import render, redirect
from .forms import PreguntasForm, Respoderform
from .models import Preguntas, Respuesta
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

class RegistroUsuario(CreateView):
    model = User
    template_name = 'registration/registrar.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')


def home(request):
    lista_preguntas=[]    
    preguntas=Preguntas.objects.all().order_by('-fechadecreacion')
    for pregunta in preguntas:
        p = {'id':pregunta.id, 'titulo':pregunta.titulo, 'descripcion': pregunta.descripcion,'respuestas':Respuesta.objects.filter(pregunta_id=pregunta.id),'usuario':User.objects.get(id=pregunta.usuario_id),'fecha': pregunta.fechadecreacion}
        lista_preguntas.append(p)
    return render(request,'index.html',{'listrapreg': lista_preguntas})


def nuevapregunta(request):
    if (request.method == 'POST'):
        form = PreguntasForm(request.POST)
        if form.is_valid():
            pregunta=form.save()
            pregunta.usuario = request.user
            pregunta.guardar()           
            redirect('home')
    else:
        form = PreguntasForm()

    return render(request,'hacerpreg.html',{'form':form})

def respueston(request,pk):
    if (request.method == 'POST'):
        form = Respoderform(request.POST)
        if form.is_valid():
            respuesta=form.save()
            pregunta=Preguntas.objects.get(id=pk) 
            respuesta.pregunta=pregunta
            respuesta.usuario = request.user
            respuesta.guardar()
            redirect('home')
    else:
        form = Respoderform()
    #mostrarid = pk
    return render(request,'responder.html',{'form':form})

