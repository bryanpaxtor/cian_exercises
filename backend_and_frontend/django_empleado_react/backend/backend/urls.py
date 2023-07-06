from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from empleado import views

router = routers.DefaultRouter()
router.register(r"empleados", views.EmpleadoView, "empleado")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
