from django.shortcuts import render
from django.http import JsonResponse
from .models import Reserva
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from .models import Departamento
from .models import Cliente
# Create view for the reservation management

def reservas(request):
    if request.method == "GET":
        reservas = Reserva.objects.all().values()
        return JsonResponse({"reservas": list(reservas)})
    
@csrf_exempt
def departamentos(request):
    if request.method == "GET":
        departamentos = Departamento.objects.all().values()
        return JsonResponse({"departamentos": list(departamentos)})
    
    elif request.method == "POST":
        data = json.loads(request.body)
        print("----------------------------------------")
        print("Esta es la data que entra al POST")
        print(data)
        nuevo_depto = Departamento.objects.create(**data)
        return JsonResponse(model_to_dict(nuevo_depto), status=201)

def clientes(request):
    if request.method == "GET":
        clientes = Cliente.objects.all().values()
        return JsonResponse({"clientes": list(clientes)})
    

def index(request):
    if request.method == "GET":
        return JsonResponse({"message": "Hello, world!"})