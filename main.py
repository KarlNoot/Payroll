from entidades.ingeniero import Ingeniero
from entidades.obrero import Obrero
from datetime import datetime
try:
    # Crear instancias de Ingeniero y Obrero solicitando sueldo diario y días trabajados
    print("Ingrese el nombre del ingeniero:")
    nombre_ingeniero = input()

    print("Ingrese los días que trabajó el ingeniero:")
    dias_trabajados_ingeniero = int(input())

    print("Ingrese el sueldo diario del ingeniero:")
    sueldo_ingeniero = float(input())

    print("Ingrese el cedula del ingeniero:")
    cedula_ingeniero = input()

    empleado1 = Ingeniero(nombre_ingeniero, datetime.now(), 500.0, sueldo_ingeniero, dias_trabajados_ingeniero, cedula_ingeniero)

    print("Ingrese el nombre del obrero:")
    nombre_obrero = input()

    print("Ingrese los días que trabajó el obrero:")
    dias_trabajados_obrero = int(input())

    print("Ingrese el sueldo diario del obrero:")
    sueldo_obrero = float(input())

    print("Ingrese la especialidad técnica del obrero:")
    especialidad_tecnica = input()

    empleado2 = Obrero(nombre_obrero, datetime.now(), 200.0, sueldo_obrero, dias_trabajados_obrero, especialidad_tecnica)

    print("------------------------------------------------------------------------------")
    print(f"Empleado: {empleado1.empleado}")
    print("Puesto: Ingeniero")
    print(f"Cédula Profesional: {empleado1.cedula_profecional}")
    # Verificar elegibilidad de bonos
    elegibilidad = empleado1.verificar_elegibilidad_bonos()
    print(f"Elegibilidad de Bonos: {elegibilidad}")
    print("sueldo Bruto:", (empleado1.dias_trabajados * empleado1.sueldo) + empleado1.bonos)
    print(f"Sueldo Neto: {empleado1.calcular_sueldo()}")
    print("fecha de emisión: ", empleado1.fecha_emision)

    print("------------------------------------------------------------------------------")
    print(f"Empleado: {empleado2.empleado}")
    print("Puesto: Obrero")
    print(f"Especialidad Técnica: {empleado2.especialidad_tecnica}")
    # Verificar elegibilidad de bonos
    elegibilidad2 = empleado2.verificar_elegibilidad_bonos()
    print(f"Elegibilidad de Bonos: {elegibilidad2}")
    print("sueldo Bruto:", (empleado2.dias_trabajados * empleado2.sueldo) + empleado2.bonos)
    print(f"Sueldo Neto: {empleado2.calcular_sueldo()}")
    print("fecha de emisión: ", empleado2.fecha_emision)

    print("------------------------------------------------------------------------------")
except ValueError:
    print("Ingrese un valor valido")
