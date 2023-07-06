from django.db import models


# Create your models here.
class Empleado(models.Model):
    # id = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=120)
    salario_base = models.DecimalField(max_digits=8, decimal_places=2)
    horas_trabajadas = models.PositiveBigIntegerField()
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
