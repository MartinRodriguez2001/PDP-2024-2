import random

class Robot:
    def __init__(self, nombre, energia):
        self.nombre = nombre
        self.energia = energia
        self.energia_actual = energia
        self.ataques = []
        self.habilidades = []

    def get_info_robot(self):
        print("----------------------")
        print(f"|NOMBRE: {self.nombre}")
        print(f"|ENERGIA: {self.energia_actual}")
        print(f"|ATAQUES: {self.get_ataques()}")
        print(f"|HABILIDADES: {self.get_habilidades()}")
        print("----------------------")
    
    def add_ataques(self, ataque):
        self.ataques.append(ataque)
    
    def get_ataques(self):
        ataques = []
        for ataque in self.ataques:
            ataques.append(ataque.get_nombre_ataque())
        return ataques
    
    def get_habilidades(self):
        habilidades = []
        for habilidad in self.habilidades:
            habilidades.append(habilidad.get_nombre_habilidad())
        return habilidades
    
    def add_habilidades(self, habilidad):
        self.habilidades.append(habilidad)
    
    def get_nombre(self):
        return self.nombre
    
    def get_energia(self):
        return self.energia
    
    def get_energia_actual(self):
        return self.energia_actual
    
    def random_ataque(self):
        return random.choice(self.ataques)
    
    def random_habilidad(self):
        return random.choice(self.habilidades)
    
    def atacar(self, robot, ataque):
        daño = ataque.get_daño()
        precision = ataque.get_precision()
        probabilidad = random.randint(10, 100)
        ataque.usar() #¿SE PUEDE USAR EL ATAQUE? FALTA VER EL TEMA DE DISMINUCION DE TURNOS RESTANTES

        if probabilidad <= precision:
            print(f"EL ATAQUE {ataque.get_nombre_ataque()} ACERTÓ")
            robot.recibir_daño(daño)
        else: 
            print(f"EL ATAQUE {ataque.get_nombre_ataque()} FALLÓ")

    def acivar_habilidad(self, evento):
        pass

    def recibir_daño(self, daño):
        self.energia_actual -= daño
    
    def reset_stats(self):
        self.energia_actual = self.energia
