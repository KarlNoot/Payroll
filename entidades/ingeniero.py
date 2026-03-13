from entidades.nomina import Nomina
from datetime import datetime

# Clase Ingeniero que hereda de Nomina
class Ingeniero(Nomina):
    def __init__(self, empleado: str, fecha_emision: datetime, bonos: float, sueldo: float, dias_trabajados: int, cedula_profecional: str):
        super().__init__(empleado, fecha_emision, bonos, sueldo, dias_trabajados)
        self.cedula_profecional = cedula_profecional
