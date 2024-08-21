import csv
import json

class Estudiantes:
    def __init__(self, nombre, edad, grado, nota_final):
        self.nombre = nombre
        self.edad = edad 
        self.grado = grado
        self.nota_final = nota_final

    def __str__(self):
        return f"ESTUDIANTE: {self.nombre}, EDAD: {self.edad}, GRADO: {self.grado}, NOTA FINAL: {self.nota_final}"
    
    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def get_grado(self):
        return self.grado
    
class Escuela:
    def __init__(self):
        self.estudiantes = []

    def cargar_estudiantes_csv(self,desde_archivo):
        with open(desde_archivo, newline ="", encoding = "utf-8") as f:
            lector = csv.reader(f)
            next(lector)
            for fila in lector:
                nombre, edad, grado, nota_final = fila
                estudiante = Estudiantes(nombre, int(edad), int(grado), int(nota_final))
                self.estudiantes.append(estudiante)
    
    def carga_estudiantes_json(self, desde_archivo):
        with open(desde_archivo, "r", enconding = "utf-8") as f:
            datos_estudiantes = json.load(f)
            for datos in datos_estudiantes:
                estudiante = Estudiantes(datos["nombre"], datos["edad"], datos["grado"], datos["nota_final"])
                self.estudiantes.append(estudiante)

    def listar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(estudiante)

    def calcular_promedio(self):
        if not self.estudiantes:
            return 0
        
        total_notas = sum(estudiante.nota_final for estudiante in self.estudiantes)
        return total_notas / len(self.estudiantes)
    
    def mejor_estudiante(self):
        if not self.estudiantes:
            return None
        return max(self.estudiantes, key=lambda e: e.nota_final)

def menu():
    escuela = Escuela()
    datos = input("INGRESA LA RUTA DE ACCESO DEL ARCHIVO: ")
    escuela.cargar_estudiantes_csv(datos)
    
    while True:

        print("GESTION DE ESTUDIANTES")
        print("1. LISTAR ESTUDIANTES: ")
        print("2. CALCULAR PROMEDIO: ")
        print("3. MEJOR ESTUDIANTE: ")
        print("4. SALIR")
        opcion = int(input("INGRESA UNA DE LAS SIGUIENTES OPCIONES: "))
        
        if opcion == 1: 
            escuela.listar_estudiantes()
        
        elif opcion == 2:
            print(escuela.calcular_promedio())
        
        elif opcion == 3:
            print(escuela.mejor_estudiante())
        
        elif opcion == 4:
            break

        else: 
            continue
menu()