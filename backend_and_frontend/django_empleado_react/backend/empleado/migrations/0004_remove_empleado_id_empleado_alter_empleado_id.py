# Generated by Django 4.2.3 on 2023-07-06 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("empleado", "0003_empleado_estado"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="empleado",
            name="id_empleado",
        ),
        migrations.AlterField(
            model_name="empleado",
            name="id",
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
