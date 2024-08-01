class alumno:
    def __init__(self, nombre, lab, t1, t2, t3):
        self.nombre = nombre
        self.lab = lab
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
    
    def get_nombre(self):
        return self.nombre
    
    def consolidado(self):
        return 0.3 * self.lab + 0.25 * self.t1 + 0.25 * self.t2 + 0.2 * self.t3
    
alumno1 = alumno("martin", 4.5, 6.0, 5.0, 4.0)
print(alumno1.get_nombre())
print(alumno1.consolidado())
