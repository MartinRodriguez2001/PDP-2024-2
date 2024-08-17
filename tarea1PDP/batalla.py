from classRobot.robot import Robot
from classRobot.ataque import Ataque
from classRobot.habilidad import Habilidad

class Batalla:
    def __init__(self, r1, r2, turnos):
        self.turnos = turnos
        self.robots = []
        self.ganador = []
        self.r1 = r1
        self.r2 = r2
    
    def iniciar_batalla(self):
        print(f"BATALLA ENTRE {self.r1.get_nombre().upper()} Y {self.r2.get_nombre().upper()} VA A COMENZAR \n")
        print("INFORMACION DE LOS PARTICIPANTES: ")
        self.r1.get_info_robot()
        self.r2.get_info_robot()

        atacante, defensor = self.r1, self.r2
        while self.r1.energia_actual > 0 and self.r2.energia_actual > 0:
            self.turno(atacante, defensor)
            atacante, defensor = defensor, atacante
            if self.r1.energia_actual > 0:
                print(f"EL GANADOR ES {self.r1.get_nombre().upper()}")
            else: 
                print(f"EL GANADOR ES {self.r2.get_nombre().upper()}")



    def turno(self, atacante, defensor):
        mov = atacante.random_ataque()
        atacante.atacar(defensor, mov)
        print(f"{atacante.get_nombre().upper()} USO {mov.get_nombre_ataque().upper()} CONTRA {defensor.get_nombre().upper()}. {defensor.get_nombre().upper()} TIENE {defensor.get_energia_actual()} DE ENERGIA")


    def finalizar_batalla(self):
        pass


diarrea = Ataque("diarrea", "liquido", "team", 5, 95, 1, 1)
diarreaexplosiva = Habilidad("diarrea explosiva", "attack_type", 2, "robot", "magic")

robot1 = Robot("el cacas", 50)
robot2 = Robot("el peos", 50)

robot1.add_ataques(diarrea)
robot1.add_habilidades(diarreaexplosiva)

robot2.add_ataques(diarrea)
robot2.add_habilidades(diarreaexplosiva)

batalla1 = Batalla(robot1, robot2, 10)
batalla1.iniciar_batalla()