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
        return render(request, "reservas.html", {"reservas": reservas})
    
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
        
        # Load all clients to verify
        clientes = Cliente.objects.all()  

        # Check if the client exists
        for cliente in clientes:
            if cliente.nombre == data['nombre'] and cliente.apellido == data['apellido']:
                return JsonResponse({'error': 'Este cliente ya existe'}, status=400)
        
        # Crea el nuevo cliente
        nuevo_cliente = Cliente.objects.create(**data)
        return JsonResponse(model_to_dict(nuevo_cliente), status=201)
    
    elif request.method == "DELETE":
        data = json.loads(request.body)
        print("----------------------------------------")
        print("Esta es la data que entra:")
        print(data)

        nombre = data.get("nombre")
        apellido = data.get("apellido")
        if not nombre or not apellido:
            return JsonResponse({'error': 'Nombre y apellido son requeridos'}, status=400)
        
        cliente = Cliente.objects.filter(nombre=nombre, apellido=apellido)
        
        if cliente.exists():
            cliente.delete()  # Elimina el cliente si existe
            return JsonResponse({'message': 'Cliente eliminado exitosamente'}, status=200)
        else:
            return JsonResponse({'error': 'Cliente no encontrado'}, status=404)

    
def index(request):
    if request.method == "GET":
        context = {
            "message": "Hello, world!"
        }
        return render(request, "index.html", context)