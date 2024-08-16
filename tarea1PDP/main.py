import json
from classRobot.robot import Robot
from classRobot.ataque import Ataque

class CargadorDatos:
    @staticmethod
    def cargar_robots(filename):
        with open(filename, 'r') as f:
            datos_robots = json.load(filename)
        robots = []
        for datos_robot in datos_robots:
            robot = Robot(datos_robot["nombre"], datos_robot["energia_maxima"])