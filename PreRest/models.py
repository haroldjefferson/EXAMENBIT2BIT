from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Preguntas(models.Model):
    titulo = models.CharField(null=False, default="", max_length=250)
    descripcion = models.TextField(null=False)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    fechadecreacion = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.titulo
    
    def guardar(self):
        self.save()
        
class Respuesta(models.Model):
    descripcion = models.TextField(null=False)
    escorrecta = models.BooleanField(default=False)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    pregunta = models.ForeignKey(Preguntas,on_delete=models.CASCADE,null=True)
    fechadecreacion = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.descripcion

    def guardar(self):
            self.save()


    
