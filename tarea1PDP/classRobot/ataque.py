class Ataque:
    def __init__(self, nombre, tipo, objetivo, daño, precision, recarga, turnos_restantes):
        self.nombre = nombre
        self.tipo = tipo
        self.objetivo = objetivo
        self.daño = daño
        self.precision = precision
        self.recarga = recarga
        self.turnos_restantes = turnos_restantes
    
    def puede_usarse(self):
        pass
    
    def usar(self):
        pass