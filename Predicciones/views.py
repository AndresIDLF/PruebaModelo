from django.shortcuts import render
from .models import Resultado

# Create your views here.
def index(request):
    return render(request,"Predicciones/index.html")

def res(request):
    Datos = Resultado.objects.all()
    return render(request,"Predicciones/resultado.html",{"Predicciones":Datos})