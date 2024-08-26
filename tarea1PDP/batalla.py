from classRobot.robot import Robot
from classRobot.ataque import Ataque
from classRobot.habilidad import Habilidad
from reporte import Reporte
import time

class Batalla:
    def __init__(self, robots):
        self.robots = robots
        self.ganador = []
        self.eleccion_personaje_usuario = None
        self.ganador = []
        self.perdedor = []

    def get_robots(self):
        return self.robots

    #ELECCION DE PERSONAJE ALEATORIO
    def batalla_aleatoria(self, r1, r2):
        print(f"BATALLA ENTRE {r1.get_nombre().upper()} Y {r2.get_nombre().upper()} VA A COMENZAR \n")
        print("INFORMACION DE LOS PARTICIPANTES: ")
        r1.get_info_robot()
        r2.get_info_robot()
        #time.sleep(2)

        atacante, defensor = r1, r2
        self.movimientos_aleatorios_1v1(atacante, defensor)
        self.resetear_stats(atacante, defensor)


    def resetear_stats(self, r1, r2):
        r1.reset_stats()
        r2.reset_stats()
    
    def movimientos_aleatorios_1v1(self, r1, r2):
        while r1.energia_actual > 0 and r2.energia_actual > 0:
            self.turno(r1, r2)
            #stime.sleep(1)
            r1, r2 = r2, r1
            self.finalizar_batalla(r1, r2)

    #ELECCION DE PERSONAJE POR EL USUARIO
    def movimientos_batalla_usuario(self):
        #MOSTRAR LISTA DE PERSONAJES DISPONIBLES
        self.eleccion_personaje_usuario = str(input("SELECCIONA TU PERSONAJE: "))

    
    def opcion_batalla(self):
        while True:
            print("INGRESE EL TIPO DE BATALLA")
            print("1. ALEATORIA")
            print("2. NORMAL (PROXIMAMENTE)")
            print("3. VOLVER")

            try:
                opcion = int(input("INGRESA EL TIPO DE BATALLA: "))
                print("\n")
                if opcion == 1:
                    r1, r2 = self.elegir_personaje()
                    self.batalla_aleatoria(r1, r2)
                    self.siguiente_pelea()

                elif opcion == 2:
                    #self.movimientos_batalla_usuario()
                    pass
                elif opcion == 3:
                    break

            except ValueError:
                print("OPCION INVALIDA. INGRESE NUEVAMENTE")
                continue
    
    def siguiente_pelea(self):
        while True:
            print("1. SIGUIENTE PELEA")
            print("2. REPORTE")
            print("3. SALIR")
            reporte1 = Reporte(self.robots)
            try:
                opcion = int(input("INGRESE UNA OPCION: "))
                print("\n")
                if opcion == 1:
                    r1, r2 = self.elegir_personaje()
                    self.batalla_aleatoria(r1, r2)
                
                elif opcion == 2:
                    reporte1.eleccion_reporte()
                
                elif opcion == 3:
                    break
            
            except ValueError:
                print("OPCION INVALIDA. INGRESE NUEVAMENTE")
                continue


    def turno(self, atacante, defensor):
        mov = atacante.random_ataque()
        atacante.atacar_robot(defensor, mov)
        print(f"{atacante.get_nombre().upper()} USO {mov.get_nombre_ataque().upper()} CONTRA {defensor.get_nombre().upper()}. {defensor.get_nombre().upper()} TIENE {defensor.get_energia_actual()} DE ENERGIA\n")

    def finalizar_batalla(self, r1, r2):
        if r1.energia_actual > 0 and r2.energia_actual <= 0:
            print(f"EL GANADOR ES {r1.get_nombre().upper()}")
            r1.add_victoria()
            r2.add_derrota()
        
        elif r1.energia_actual <= 0 and r2.energia_actual > 0:
            print(f"EL GANADOR ES {r2.get_nombre().upper()}")
            r2.add_victoria()
            r1.add_derrota()
    
    
    def get_nombres_robots(self):
        return self.robots
    


#ALGO RARO TIENE ESTO, NO LO HE REVISADO, PROBABLEMENTE TENGA ALGO MALO 
    def elegir_ataque(self, robot):
        while True:
            print(f"ATAQUES DISPONIBLES: {robot.get_ataques()}")
            nombres = [robot.get_ataques() for robot in self.robots]
            for idx, nombre in enumerate(nombres, start = 1):
                print(f"{idx}. {nombre}")
            try:
                preguntar_ataque = int(input("INGRESE EL ATAQUE DE DESEA UTILIZAR: "))

                if preguntar_ataque < 0 or preguntar_ataque >= len(self.robots):
                    print("SELECCION INVALIDA. INGRESE NUEVAMENTE")
            
                ataque = self.robots[preguntar_ataque] #AQUI
                return ataque
            
            except ValueError:
                print("ERROR: LA ENTRADA NO CORRESPONDE")
                continue


    def elegir_personaje(self):
        while True:
            print("LISTA DE PERSONAJES DISPONIBLES:")
            nombres = [robot.get_nombre() for robot in self.robots]
            for idx, nombre in enumerate(nombres, start=1):
                print(f"{idx}. {nombre}")
            try:   
                seleccion1 = int(input("SELECCIONA EL PRIMER PERSONAJE (INGRESA EL NUMERO)): ")) - 1
                seleccion2 = int(input("SELECCIONA EL SEGUNDO PERSONAJE (INGRESA EL NUMERO): ")) - 1

                if seleccion1 < 0 or seleccion1 >= len(self.robots) or seleccion2 < 0 or seleccion2 >= len(self.robots):
                    print("SELECCION INVALIDA. INGRESE NUEVAMENTE")
                    continue
                    
                if seleccion1 == seleccion2:
                    print("NO SE PUEDE SELECCIONAR EL MISMO PERSONAJE")
                    continue

                personaje1 = self.robots[seleccion1]
                personaje2 = self.robots[seleccion2]
                
                return personaje1, personaje2
            
            except ValueError:
                print("ERROR: LA ENTRADA NO CORRESPONE")
                continue


