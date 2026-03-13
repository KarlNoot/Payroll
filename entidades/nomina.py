from datetime import datetime

# Clase Nomina que representa la nómina de un empleado
class Nomina:
    def __init__(self, empleado: str, fecha_emision: datetime, bonos: float, sueldo: float, dias_trabajados: int):
        self.empleado = empleado
        self.fecha_emision = fecha_emision
        self.bonos = bonos
        self.sueldo = sueldo
        self.dias_trabajados = dias_trabajados
        # bono_puntualidad puede ser 0 por defecto; subclasses pueden ajustarlo si es necesario
        self.bono_puntualidad = 0.0

    def deducir_impuestos(self, sueldo_bruto: float) -> float:
        """Devuelve el sueldo neto después de descontar el 16% de impuestos del sueldo bruto."""
        tasa = 0.16
        impuesto = sueldo_bruto * tasa
        return sueldo_bruto - impuesto

    def puede_recibir_bonos(self) -> bool:
        """Verifica si el empleado puede recibir bonos.
        Condiciones: 
        - Mínimo de 20 días trabajados
        - No puede tener ninguna falta injustificada
        """
        dias_minimos = 20
        return self.dias_trabajados >= dias_minimos

    def verificar_elegibilidad_bonos(self) -> str:
        """Verifica si el empleado puede recibir bonos."""
        es_elegible = self.puede_recibir_bonos()
        if es_elegible:
            return f"Empleado SI puede recibir bonos (Trabajó {self.dias_trabajados} de 20)"
        else:
            return f"Empleado NO puede recibir bonos (Trabajó {self.dias_trabajados} de 20)"

    def calcular_sueldo(self) -> float:
        """Calcula el sueldo neto: aplica impuestos al sueldo bruto y luego suma el bono de puntualidad."""
        sueldo_bruto = (self.dias_trabajados * self.sueldo) + self.bonos
        sueldo_neto = self.deducir_impuestos(sueldo_bruto)
        return sueldo_neto + self.bono_puntualidad
