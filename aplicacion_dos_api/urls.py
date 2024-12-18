"""point_experts_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aplicacion_dos_api.views import bootstrap
from aplicacion_dos_api.views import users,maestros,alumnos,materias
from aplicacion_dos_api.views import auth

urlpatterns = [
    #Version
        path('bootstrap/version', bootstrap.VersionView.as_view()),
    #Create Admin
        path('admin/', users.AdminView.as_view()),
    #Create Maestro
        path('maestros/',maestros.MaestrosView.as_view()),
    #Create alumno
        path('alumnos/',alumnos.AlumnosView.as_view()),
    #Login
        path('token/', auth.CustomAuthToken.as_view()),
    #Logout
        path('logout/', auth.Logout.as_view()),
    #Admin Data
        path('lista-admins/', users.AdminAll.as_view()),
    #Maestro Data
        path('lista-maestros/', maestros.MaestrosAll.as_view()),
    #Alumno Data
        path('lista-alumnos/', alumnos.AlumnosAll.as_view()),
        path('admins-edit/', users.AdminsViewEdit.as_view()),
        path('maestros-edit/', maestros.MaestrosViewEdit.as_view()),
        path('alumnos-edit/', alumnos.AlumnosViewEdit.as_view()),
    #Materia Data
        path('materias/',materias.MateriasView.as_view()),
        path('lista-materias/',materias.MateriasAll.as_view()),
        path('materias-edit/',materias.MateriasViewEdit.as_view())
]
