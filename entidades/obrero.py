from entidades.nomina import Nomina
from datetime import datetime


class Obrero(Nomina):
    def __init__(self, empleado: str, fecha_emision: datetime, bonos: float, impuestos: float, salario_obrero: int):
        super().__init__(self, empleado, fecha_emision, bonos, impuestos)
        self.salario_obrero = salario_obrero
        
