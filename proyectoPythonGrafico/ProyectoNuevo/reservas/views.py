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
    
    elif request.method == "POST":
        data = json.loads(request.body)
        print("----------------------------------------")
        print("Esta es la data que entra al POST")
        print(data)
        # Create a new reservation
        # Validations
        # 1. The start date must be before the end date
        nueva_reserva = Reserva.objects.create(**data)
        if nueva_reserva.fecha_inicio > nueva_reserva.fecha_fin:
            return JsonResponse({"error": "La fecha de inicio debe ser anterior a la fecha de fin"}, status=400)
        # 2. Verify that number of people is grater than 2
        if not nueva_reserva.cantidad_de_personas >= 2:
            return JsonResponse({'error' : 'La cantidad de personas ingresada no es correcta'}, status = 400)

        return JsonResponse(model_to_dict(nueva_reserva), status=201)

       
    
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


@csrf_exempt
def clientes(request):
    if request.method == "GET":
        clientes = Cliente.objects.all().values()
        return JsonResponse({"clientes": list(clientes)})

    elif request.method == "POST":
        data = json.loads(request.body)
        print("----------------------------------------")
        print("Esta es la data que entra al POST")
        print(data)
        
        # Carga todos los clientes para la validación
        clientes = Cliente.objects.all()  

        # Verifica si el cliente ya existe
        for cliente in clientes:
            if cliente.nombre == data['nombre'] and cliente.apellido == data['apellido']:
                return JsonResponse({'error': 'Este cliente ya existe'}, status=400)
        
        # Crea el nuevo cliente
        nuevo_cliente = Cliente.objects.create(**data)
        return JsonResponse(model_to_dict(nuevo_cliente), status=201)
    
def index(request):
    if request.method == "GET":
        context = {
            "message": "Hello, world!"
        }
        return render(request, "index.html", context)