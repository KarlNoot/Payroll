from entidades.ingeniero import Ingeniero
from entidades.obrero import Obrero
from datetime import datetime
try:

    print("Sistema de nomina de Maquiladora")
    print("Ingresa el pago que se dara por bono de puntualidad para el ingeniero:")
    bono_ingeniero = float(input())
    print("Ingresa el pago que se dara por bono de puntualidad para el obrero:")
    bono_obrero = float(input())

    print("Ingresa la información de los empleados para calcular su nómina")
    # Crear instancias de Ingeniero y Obrero solicitando sueldo diario y días trabajados
    print("Ingrese el nombre del ingeniero:")
    nombre_ingeniero = input()

    print("Ingrese los días que trabajó el ingeniero:")
    dias_trabajados_ingeniero = int(input())

    print("Ingrese el sueldo diario del ingeniero:")
    sueldo_ingeniero = float(input())

    print("")
    empleado1 = Ingeniero(nombre_ingeniero, datetime.now(), bono_ingeniero, sueldo_ingeniero, dias_trabajados_ingeniero)

    print("Ingrese el nombre del obrero:")
    nombre_obrero = input()

    print("Ingrese los días que trabajó el obrero:")
    dias_trabajados_obrero = int(input())

    print("Ingrese el sueldo diario del obrero:")
    sueldo_obrero = float(input())

    empleado2 = Obrero(nombre_obrero, datetime.now(), bono_obrero, sueldo_obrero, dias_trabajados_obrero)

    print("------------------------------------------------------------------------------")
    print(f"Empleado: {empleado1.empleado}")
    print("Puesto: Ingeniero")
    # Verificar elegibilidad de bonos
    elegibilidad = empleado1.verificar_elegibilidad_bonos()
    print(f"Elegibilidad de Bonos:{elegibilidad['mensaje']}")
    print("sueldo Bruto:", (empleado1.dias_trabajados * empleado1.sueldo) + empleado1.bonos)
    print(f"Sueldo Neto: {empleado1.calcular_sueldo()}")
    print("fecha de emisión: ", empleado1.fecha_emision)

    print("------------------------------------------------------------------------------")
    print(f"Empleado: {empleado2.empleado}")
    print("Puesto: Obrero")
    # Verificar elegibilidad de bonos
    elegibilidad2 = empleado2.verificar_elegibilidad_bonos()
    print(f"Elegibilidad de Bonos:{elegibilidad2['mensaje']}")
    print("sueldo Bruto:", (empleado2.dias_trabajados * empleado2.sueldo) + empleado2.bonos)
    print(f"Sueldo Neto: {empleado2.calcular_sueldo()}")
    print("fecha de emisión: ", empleado2.fecha_emision)

    print("------------------------------------------------------------------------------")

except ValueError:
    print("Ingresa un valor valido")
