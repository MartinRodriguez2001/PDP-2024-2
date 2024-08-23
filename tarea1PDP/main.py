import json
from classRobot.robot import Robot
from classRobot.ataque import Ataque
class RobotLoader:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def cargar_robots(self):
        with open(self.nombre_archivo, 'r') as archivo:
            datos = json.load(archivo)
        
        robots = []

        for robot_data in datos['robots']:
            # Crear instancia de Robot
            robot = Robot(robot_data['name'], robot_data['energy'])
            
            # Crear instancias de Ataque y agregarlos al robot
            for ataque_data in robot_data['attacks']:
                ataque = Ataque(
                    ataque_data['name'],
                    ataque_data['type'],
                    ataque_data['objective'],
                    ataque_data['damage'],
                    ataque_data['precision'],
                    ataque_data['recharge']
                )
                robot.ataques.append(ataque)

            # Aquí puedes agregar lógica para las habilidades si las necesitas

            robots.append(robot)

        return robots

nombre_archivo = '/Users/martinrodriguez/PDP-2024-2/tarea1PDP/data.json'  # Asegúrate de que este archivo exista y contenga datos válidos
loader = RobotLoader(nombre_archivo)
robots = loader.cargar_robots()
