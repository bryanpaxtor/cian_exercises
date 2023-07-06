from django.shortcuts import render
from rest_framework import viewsets
from .models import Empleado
from .serializers import EmpleadoSerializer


class EmpleadoView(viewsets.ModelViewSet):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()
