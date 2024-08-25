class Ataque:
    def __init__(self, nombre, tipo, objetivo, daño, precision, recarga, turnos_restantes = 0):
        #indica el nombre del ataque
        self.nombre = nombre
        #long o sword o hand
        self.tipo = tipo 
        #team o robot
        self.objetivo = objetivo  
        #int cuanto daño hace el ataque
        self.daño = daño 
        #int porcentaje que indica la cantidad de veces que el ataque acierta su objetivo
        self.precision = precision 
        #int cuantos turnos debe esperar antes de poder volver a usar este ataque
        self.recarga = recarga
        #int que muestra cuantos turnos le faltan para volver a usar el ataque
        self.turnos_restantes = turnos_restantes

    def get_nombre_ataque(self):
        return self.nombre

    def get_tipo_ataque(self):
        return self.tipo

    def get_objetivo_ataque(self):
        return self.objetivo
    
    def get_daño(self):
        return self.daño
    
    def get_precision(self):
        return self.precision
    
    def get_recarga(self):
        return self.recarga
    
    def get_turnos_restantes(self):
        return self.turnos_restantes
    
    def puede_usarse(self):
        if self.turnos_restantes == 0:
            return True
        else:
            return False
    
    def ataque_robot(self):
        if self.objetivo == "robot":
            return True
        elif self.objetivo == "team":
            return False
        else: 
            return True
        
    def usar(self):
        if self.puede_usarse() == True:
            self.turnos_restantes = self.turnos_restantes + self.recarga
            return self.daño
        else:
            return f"EL ATAQUE {self.nombre.upper()} NO PUEDE USARSE, SE ESTA RECARGANDO. TURNOS RESTANTES: {self.turnos_restantes}"

