# Generated by Django 4.2.3 on 2023-07-06 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("id_empleado", models.CharField(max_length=20, unique=True)),
                ("nombre", models.CharField(max_length=120)),
                ("salario_base", models.DecimalField(decimal_places=2, max_digits=8)),
                ("horas_trabajadas", models.PositiveBigIntegerField()),
            ],
        ),
    ]