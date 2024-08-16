class Habilidad:
    def __init__(self, nombre, activador, duracion, objetivo, efecto, activo):
        self.nombre = nombre
        self.activador = activador
        self.duracion = duracion
        self.objetivo = objetivo
        self.efecto = efecto
        self.activo = activo
    
    def activar(self):
        pass

    def desactivar(self):
        pass

    def aplicar_efecto(self, robot):
        pass
    

