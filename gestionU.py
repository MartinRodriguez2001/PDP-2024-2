class Curso:
    def __init__(self, nombre, hora, cupos, dia):
        self.nombre = nombre
        self.hora = hora
        self.cupos = cupos
        self.dia = dia
        self.estudiantes = []
        self.profesores = []

    def informaciónCurso(self):
        return f'{self.nombre} SE IMPARTIRÁ EL DIA {self.dia} A LAS {self.hora}.'
    def cuposActuales(self):
        return f'QUEDAN {self.cupos} CUPOS'
    
    def agregarEstudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        self.cupos -=1
        if self.cupos == 0:
            print("No quedan mas cupos en el curso")

    
    def agregarProfessor(self, profesor):
        self.profesores.append(profesor)

class Professor:
    def __init__(self, nombre):
        self.nombre = nombre

class Student:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []
        self.inscripciones = []
    
    def inscrbirCurso(self, curso):
        self.inscripciones.append(curso)
    
    def mostrarInscripciones(self):
        return self.inscripciones

pdp = Curso("Paradigmas de Programación", "18:00", 3, "Jueves")
profe1 = Professor("Matias Recabarren")
estudiante = Student("martin")
estudiante.inscrbirCurso(pdp)
pdp.agregarEstudiante(estudiante)
pdp.agregarProfessor(profe1)
print(pdp.cuposActuales())
print(pdp.informaciónCurso())
print(estudiante.mostrarInscripciones())
