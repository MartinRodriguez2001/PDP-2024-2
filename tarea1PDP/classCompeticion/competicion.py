from batalla import Batalla
class Competicion:
    def __init__(self, robots):
        self.robots = robots
        self.resultados = {}
    
    def iniciar_competencia(self):
        batalla1 = Batalla(self.robots)
        batalla1.opcion_batalla()



    def registrar_resultado(self, ganadores_lista, perdedores_lista):
            pass