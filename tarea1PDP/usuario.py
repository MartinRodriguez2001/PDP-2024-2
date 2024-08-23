from classRobot.robot import Robot
from classRobot.ataque import Ataque
from batalla import Batalla
from main import RobotLoader

class Usuario:
    def __init__(self):
        self.historial_acciones = []
        self.modo_juego = None
    
    def opcion_menu(self):
        while True:
            print("----PELEAS DE ROBOTS EN VIVO----")
            print("SELECCIONAR TIPO DE PELEA")
            print("1. COMBATE 1 VS 1")
            print("2. LIGA")
            print("3. PLAYOFF (PROXIMAMENTE)")
            print("4. TORNEO (PROXIMAMENTE)")  
            print("5. SALIR")

            self.modo_juego = int(input("INGRESE UNA OPCION: "))
            print("\n")
            nombre_archivo = '/Users/martinrodriguez/PDP-2024-2/tarea1PDP/data.json'  # Asegúrate de que este archivo exista y contenga datos válidos
            loader = RobotLoader(nombre_archivo)
            robots = loader.cargar_robots()

            if self.modo_juego == 1:
                batalla1 = Batalla(robots)
                batalla1.iniciar()

            elif self.modo_juego == 2:
                print("EL MODO ESTARÁ PROXIMAMENTE\n")
                pass
            elif self.modo_juego == 3:
                print("EL MODO ESTARÁ PROXIMAMENTE\n")
                pass
            elif self.modo_juego == 4:
                print("EL MODO ESTARÁ PROXIMAMENTE\n")
                pass
            elif self.modo_juego == 5:
                break
            else: 
                print("OPCION INVALIDA. VUELVA A SELECCIONAR UNA OPCION\n")
                continue
            
usuario1 = Usuario()
usuario1.opcion_menu()