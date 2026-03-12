from entidades import nomina
from entidades.ingeniero import Ingeniero
from entidades.obrero import Obrero
from datetime import datetime

# Crear instancias de Ingeniero y Obrero solicitando sueldo diario y días trabajados
print("Ingrese el nombre del ingeniero:")
nombre_ingeniero = input()

print("Ingrese los días que trabajó el ingeniero:")
dias_trabajados_ingeniero = int(input())

print("Ingrese el sueldo diario del ingeniero:")
sueldo_ingeniero = float(input())

empleado1 = Ingeniero(nombre_ingeniero, datetime.now(), 500.0, sueldo_ingeniero, dias_trabajados_ingeniero)

print("Ingrese el nombre del obrero:")
nombre_obrero = input()

print("Ingrese los días que trabajó el obrero:")
dias_trabajados_obrero = int(input())

print("Ingrese el sueldo diario del obrero:")
sueldo_obrero = float(input())

empleado2 = Obrero(nombre_obrero, datetime.now(), 200.0, sueldo_obrero, dias_trabajados_obrero)

print("------------------------------------------------------------------------------")
print(f"Empleado: {empleado1.empleado}")
print("Puesto: Ingeniero")
print("sueldo Bruto:", (empleado1.dias_trabajados * empleado1.sueldo) + empleado1.bonos)
print(f"Sueldo Neto: {empleado1.calcular_sueldo()}")
print("fecha de emisión: ", empleado1.fecha_emision)

print("------------------------------------------------------------------------------")
2
print(f"Empleado: {empleado2.empleado}")
print("Puesto: Obrero")
print("sueldo Bruto:", (empleado2.dias_trabajados * empleado2.sueldo) + empleado2.bonos)
print(f"Sueldo Neto: {empleado2.calcular_sueldo()}")
print("fecha de emisión: ", empleado2.fecha_emision)

print("------------------------------------------------------------------------------")