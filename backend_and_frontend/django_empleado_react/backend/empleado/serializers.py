from rest_framework import serializers
from .models import Empleado


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ("id", "nombre", "salario_base", "horas_trabajadas", "estado")
