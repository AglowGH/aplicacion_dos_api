from rest_framework import serializers
from rest_framework.authtoken.models import Token
from aplicacion_dos_api.models import *

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id','first_name','last_name', 'email')

class AdminSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Administradores
        fields = '__all__'


class MaestroSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Maestros
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Alumnos
        fields = "__all__"

class MateriaSerializer(serializers.ModelSerializer):
     class Meta:
        model = Materias
        fields = ['nrc','nombre','seccion','salon','programa_educativo','profesor_asignado','creditos','hora_inicio','minuto_inicio','hora_fin','minuto_fin']