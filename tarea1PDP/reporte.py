import csv
class Reporte:
    def __init__(self, robots):
        self.robots = robots
        self.datos = {}
    
    def generar_reporte(self):
        pass

    def guardar_reporte(self, formato):
        pass

    def eleccion_reporte(self):
        while True:
            print("REPORTES DE PELEAS")
            print("1. REPORTE DE VICTORIAS/DERROTAS")
            print("2. GRAFICO DE BARRAS ATAQUES (PROXIMAMENTE)")
            print("3. GRAFICO DE BARRAS HABILIDAD (PROXIMAMENTE)")
            print("4. TABLA DE BATALLAS (PROXIMAMENTE)")
            print("5. VOLVER")

            try:
                opcion = int(input("SELECCIONA LOS REPORTES QUE DESEAS VISUALIZAR"))
                print("\n")
                
                if opcion == 1:
                    datos = self.ordenar_lista()
                    self.reporte_victorias_derrotas(datos)

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

    def reporte_victorias_derrotas(self, datos):
        nombre_archivo = "tabla_victorias_derrotas.csv"
        encabezados = ["NOMBRE", "VICTORIAS"]

        with open(nombre_archivo, mode ="w", newline="") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(encabezados)
            writer.writerow("\n")
            
            for fila in datos:
                writer.writerow(fila)
                archivo.write("\n")

        print(f"EL ARCHIVO {nombre_archivo} SE HA CARGADO CORRECTAMENTE")

    def reporte_grafico_ataques(self):
        pass

    def reporte_grafico_habilidad(self):
        pass

    def tablas_batallas(self):
        pass

    def ordenar_lista(self):
        self.robots.sort(key= lambda x: x.victorias, reverse = True)
        lista_ordenados = [[robot.nombre, robot.victorias] for robot in self.robots]
        return lista_ordenados
