class Habilidad:
    def __init__(self, nombre, activador, duracion, objetivo, efecto):
        self.nombre = nombre
        self.activador = activador
        self.duracion = duracion
        self.objetivo = objetivo
        self.efecto = efecto
        self.activo = bool
    
    def get_nombre_habilidad(self):
        return self.nombre
    
    def isActive(self):
        return self.activo
    
    def activar(self):
        return self.activo == True

    def desactivar(self):
        return self.activo == False

    def aplicar_efecto(self, robot):
        pass
    

