from classRobot.robot import Robot
from classRobot.ataque import Ataque
from classRobot.habilidad import Habilidad
import time

class Batalla:
    def __init__(self, robots):
        self.robots = robots
        self.ganador = []
        self.eleccion_personaje_usuario = None
        self.opcion = None
    

    #ELECCION DE PERSONAJE ALEATORIO
    def movimientos_batalla_aleatoria(self, r1, r2):
        print(f"BATALLA ENTRE {r1.get_nombre().upper()} Y {r2.get_nombre().upper()} VA A COMENZAR \n")
        print("INFORMACION DE LOS PARTICIPANTES: ")
        r1.get_info_robot()
        r2.get_info_robot()

        atacante, defensor = r1, r2
        while r1.energia_actual > 0 and r2.energia_actual > 0:
            self.turno(atacante, defensor)
            time.sleep(1)
            atacante, defensor = defensor, atacante
            self.finalizar_batalla(r1, r2)

    #ELECCION DE PERSONAJE POR EL USUARIO
    def movimientos_batalla_usuario(self):
        #MOSTRAR LISTA DE PERSONAJES DISPONIBLES
        self.eleccion_personaje_usuario = str(input("SELECCIONA TU PERSONAJE: "))

    
    def opcion_batalla(self):
        while True:
            print("INGRESE EL TIPO DE BATALLA")
            print("1. ALEATORIA")
            print("2. NORMAL")
            print("3. VOLVER")

            self.opcion = int(input("INGRESA EL TIPO DE BATALLA: "))
            print("\n")
            if self.opcion == 1:
                r1, r2 = self.elegir_personaje()
                self.movimientos_batalla_aleatoria(r1, r2)
            elif self.opcion == 2:
                self.movimientos_batalla_usuario()
            elif self.opcion == 3:
                break
    
    def iniciar(self):
        self.opcion_batalla()

    def turno(self, atacante, defensor):
        mov = atacante.random_ataque()
        atacante.atacar(defensor, mov)
        print(f"{atacante.get_nombre().upper()} USO {mov.get_nombre_ataque().upper()} CONTRA {defensor.get_nombre().upper()}. {defensor.get_nombre().upper()} TIENE {defensor.get_energia_actual()} DE ENERGIA")


    def finalizar_batalla(self, r1, r2):
        if r1.energia_actual > 0 and r2.energia_actual <= 0:
            print(f"EL GANADOR ES {r1.get_nombre().upper()}")
        elif r1.energia_actual <= 0 and r2.energia_actual > 0:
            print(f"EL GANADOR ES {r2.get_nombre().upper()}")
    
    def get_nombres_robots(self):
        return self.robots

    def elegir_ataque(self, robot):
        print(f"ATAQUES DISPONIBLES: {robot.get_ataques()}")
        self.preguntar_ataque = input("INGRESE EL ATAQUE DE DESEA UTILIZAR: ")
    
    def elegir_personaje(self):
        print("Lista de personajes disponibles:")
        nombres = [robot.get_nombre() for robot in self.robots]
        for idx, nombre in enumerate(nombres, start=1):
            print(f"{idx}. {nombre}")
    
        seleccion1 = int(input("Selecciona el primer personaje (ingresa el número): ")) - 1
        seleccion2 = int(input("Selecciona el segundo personaje (ingresa el número): ")) - 1

        if seleccion1 < 0 or seleccion1 >= len(self.robots) or seleccion2 < 0 or seleccion2 >= len(self.robots):
            print("Selección no válida. Por favor selecciona números válidos de la lista.")
            return None, None
        
        if seleccion1 == seleccion2:
            print("No puedes seleccionar el mismo personaje dos veces.")
            return None, None
        
        personaje1 = self.robots[seleccion1]
        personaje2 = self.robots[seleccion2]
        
        return personaje1, personaje2


