class Reporte:
    def __init__(self, tipo):
        self.tipo = tipo
        self.datos = {}
    
    def generar_reporte(self):
        pass

    def guardar_reporte(self, formato):
        pass

    def eleccion_reporte(self):
        while True:
            print("REPORTES DE PELEAS")
            print("1. REPORTE DE VICTORIAS/DERROTAS")
            print("2. GRAFICO DE BARRAS ATAQUES")
            print("3. GRAFICO DE BARRAS HABILIDAD")
            print("4. TABLA DE BATALLAS")
            print("5. VOLVER")

            try:
                opcion = int(input("SELECCIONA LOS REPORTES QUE DESEAS VISUALIZAR"))
                print("\n")
                
                if opcion == 1:
                    pass
                elif opcion == 2:
                    pass
                elif opcion == 3:
                    pass
                elif opcion == 4:
                    pass
                elif opcion == 5:
                    break

            except ValueError:
                print("OPCION INVALIDA. INGRESA NUEVAMENTE")
                continue

    def reporte_victorias_derrotas(self):
        pass

    def reporte_grafico_ataques(self):
        pass

    def reporte_grafico_habilidad(self):
        pass

    def tablas_batallas(self):
        pass
