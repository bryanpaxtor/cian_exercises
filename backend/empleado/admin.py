from django.contrib import admin
from .models import Empleado


# Register your models here.
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "salario_base",
        "horas_trabajadas",
        "estado",
    )


admin.site.register(Empleado, EmpleadoAdmin)
