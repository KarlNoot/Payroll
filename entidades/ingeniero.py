from entidades.nomina import Nomina
from datetime import datetime


class Ingeniero(Nomina):
    def __init__(self, empleado: str, fecha_emision: datetime, bonos: float, impuestos: float, salario_ingeniero: int):
        super().__init__(self, empleado, fecha_emision, bonos, impuestos)
        self.salario_ingeniero = salario_ingeniero

    
