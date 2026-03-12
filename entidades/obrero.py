from entidades.nomina import Nomina
from datetime import datetime

# Clase Obrero que hereda de Nomina
class Obrero(Nomina):
    def __init__(self, empleado: str, fecha_emision: datetime, bonos: float, sueldo: float, dias_trabajados: int):
        super().__init__(empleado, fecha_emision, bonos, sueldo, dias_trabajados)
