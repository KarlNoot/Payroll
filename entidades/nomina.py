from datetime import datetime

class Nomina:
    def __init__(self, empleado: str, fecha_emision: datetime, bonos: float, impuestos: float):
        self.empleado = empleado        
        self.fecha_emision = fecha_emision
        self.bonos = bonos
        self.impuestos = impuestos

    def deducir_impuestos(self) -> float:
        