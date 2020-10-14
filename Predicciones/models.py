from django.db import models

class Resultado(models.Model):
    Num_count=models.CharField(max_length=100,primary_key=True)
    ID_Imagen=models.CharField(max_length=100)
    Clase_Prediccion=models.CharField(max_length=20)
    Porcentaje_Clase1=models.FloatField(null=True, blank=True, default=None)
    Porcentaje_Clase2=models.FloatField(null=True, blank=True, default=None)


