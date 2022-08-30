from django.db import models

class Familiares(models.Model):
    nombre=models.CharField(max_length=50)
    dni=models.IntegerField()
    fecha_nacimiento=models.DateField()

