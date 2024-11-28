from django.shortcuts import render
from django.db.models import *
from django.db import transaction
from aplicacion_dos_api.serializers import *
from aplicacion_dos_api.models import *
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.utils.html import strip_tags
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from datetime import datetime
from django.conf import settings
from django.template.loader import render_to_string
import string
import random
import json

class MateriasAll(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        materias = Materias.objects.all()
        materias = MateriaSerializer(materias, many=True).data
        for materia in materias:
            materia["dias"] = json.loads(materia["dias"])
        return Response(materias, 200)


class MateriasView(generics.CreateAPIView):
    #Obtener usuario por ID
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        materia = get_object_or_404(Materias, nrc = request.GET.get("nrc"))
        materia = MateriaSerializer(materia, many=False).data
        materia["dias"] = json.loads(materia["dias"])
        return Response(materia, 200)
    
    #Registrar nuevo usuario
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        request.data['dias'] = json.dumps(request.data['dias'])
        materia = MateriaSerializer(data=request.data)
        if materia.is_valid():
            nrc = request.data['nrc']
            #Valida si existe el nrc registrado
            existing_subject = Materias.objects.filter(nrc=nrc).first()

            if existing_subject:
                return Response({"message":"nrc "+ nrc +", is already taken"},400)
            
            #Create a subject
            materia = Materias.objects.create(
                        nrc = request.data['nrc'],
                        nombre = request.data['nombre'],
                        seccion = request.data['seccion'],
                        salon =request.data['salon'],
                        programa_educativo = request.data['programa_educativo'],
                        profesor_asignado = request.data['profesor_asignado'],
                        creditos = request.data['creditos'],
                        hora_inicio = request.data['hora_inicio'],
                        minuto_inicio = request.data['minuto_inicio'],
                        hora_fin = request.data['hora_fin'],
                        minuto_fin = request.data['minuto_fin'],
                        dias = request.data['dias']
                    )
            materia.save()

            return Response({"materia nrc: ": materia.nrc }, 201)

        return Response(materia.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MateriasViewEdit(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    #def put(self, request, *args, **kwargs):
        # iduser=request.data["id"]
        #materia = get_object_or_404(Materias, id=request.data["nrc"])
        #maestro.id_trabajador = request.data["id_trabajador"]
        #maestro.fecha_nacimiento = request.data["fecha_nacimiento"]
        #maestro.telefono = request.data["telefono"]
        #maestro.rfc = request.data["rfc"]
        #maestro.cubiculo = request.data["cubiculo"]
        #maestro.area_investigacion = request.data["area_investigacion"]
        #maestro.materias_json = json.dumps(request.data["materias_json"])
        #maestro.save()
        #temp = maestro.user
        #temp.first_name = request.data["first_name"]
        #temp.last_name = request.data["last_name"]
        #temp.save()
        #user = MaestroSerializer(maestro, many=False).data
        #return Response(user,200)
    
    def delete(self, request, *args, **kwargs):
        materia = get_object_or_404(Materias, nrc=request.GET.get("nrc"))
        try:
            materia.delete()
            return Response({"details":"Maestro eliminado"},200)
        except Exception as e:
            return Response({"details":"Algo pasó al eliminar"},400)