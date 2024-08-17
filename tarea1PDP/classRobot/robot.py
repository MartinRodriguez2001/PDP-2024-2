import random
from ataque import Ataque
from habilidad import Habilidad

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
    
    def get_name(self):
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
        energia_atacado = robot.get_energia_actual()
        energia_atacado = energia_atacado - daño

    def acivar_habilidad(self, evento):
        pass

    def recibir_daño(self, daño):
        self.energia = self.energia - daño

diarrea = Ataque("diarrea", "liquido", "team", 5, 95, 1, 1)
diarreaexplosiva = Habilidad("diarrea explosiva", "attack_type", 2, "robot", "magic")
robot1 = Robot("el cacas", 50)
robot2 = Robot("el peos", 50)
robot1.add_ataques(diarrea)
robot1.add_habilidades(diarreaexplosiva)

robot2.add_ataques(diarrea)
robot2.add_habilidades(diarreaexplosiva)

robot1.get_info_robot()
robot2.get_info_robot()

robot1.atacar(robot2, diarrea)
robot2.get_info_robot()