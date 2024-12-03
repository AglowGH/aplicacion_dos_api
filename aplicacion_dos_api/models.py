from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings

class BearerTokenAuthentication(TokenAuthentication):
    keyword = u"Bearer"


#class Profiles(models.Model):
#    id = models.BigAutoField(primary_key=True)
#    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
#    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#    update = models.DateTimeField(null=True, blank=True)
#
#    def __str__(self):
#        return "Perfil del usuario "+self.usuario.first_name+" "+self.usuario.last_name

class Administradores(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    clave_admin = models.CharField(max_length=255,null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    rfc = models.CharField(max_length=255,null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    ocupacion = models.CharField(max_length=255,null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Perfil del admin "+self.first_name+" "+self.last_name


class Maestros(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    id_trabajador = models.CharField(max_length=255,null=True, blank=True)
    fecha_nacimiento = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    rfc = models.CharField(max_length=255,null=True, blank=True)
    cubiculo = models.CharField(max_length=255,null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    area_investigacion = models.CharField(max_length=255,null=True, blank=True)
    materias_json = models.TextField(null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Perfil del maestro "+self.first_name+" "+self.last_name
    
class Alumnos(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    matricula = models.CharField(max_length=255,null=True, blank=True)
    curp = models.CharField(max_length=255,null=True, blank=True)
    rfc = models.CharField(max_length=255,null=True, blank=True)
    fecha_nacimiento = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    ocupacion = models.CharField(max_length=255,null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Perfil del alumno "+self.first_name+" "+self.last_name
    
class Materias(models.Model):
    nrc = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255,null=True, blank=True)
    seccion = models.IntegerField(null=True, blank=True)
    salon = models.CharField(max_length=255,null=True, blank=True)
    programa_educativo = models.CharField(max_length=255,null=True, blank=True)
    profesor_asignado =  models.ForeignKey(Maestros, on_delete=models.CASCADE, null=False, blank=False, default=None)
    creditos = models.IntegerField(null=True, blank=True)
    hora_inicio = models.IntegerField(null=True, blank=True)
    minuto_inicio = models.IntegerField(null=True, blank=True)
    hora_fin = models.IntegerField(null=True, blank=True)
    minuto_fin = models.IntegerField(null=True, blank=True)
    dias = models.TextField(null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"NRC: {self.nrc}"
    
    #['nrc','nombre','seccion','salon','programa_educativo','profesor_asignado','creditos','hora_inicio','minuto_inicio','hora_fin','minuto_fin','dias']