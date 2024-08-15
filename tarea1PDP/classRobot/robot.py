class Robot:
    def __init__(self, nombre, energia, energia_actual, ataques, habilidades):
        self.nombre = nombre
        self.energia = energia
        self.energia_actual = energia_actual
        self.ataques = ataques
        self.habilidades = habilidades
    
    def atacar(self, robot, ataque):
        pass

    def acivar_habilidad(self, evento):
        pass

    def recibir_daño(self, daño):
        pass