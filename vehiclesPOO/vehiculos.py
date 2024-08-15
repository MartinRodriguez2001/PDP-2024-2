from abc import ABC, abstractmethod
import json

class Vehicle:
    def __init__(self, type, brand, model, year, color, fuel):
        self.type = type
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.fuel = fuel
    def __str__(self):
        return f"{self.type} - {self.brand} {self.model} ({self.year}), Color: {self.color}, Combustible: {self.fuel}"

class Car(Vehicle):
    def __init__(self, type, brand, model, year, color, fuel, doors):
        super().__init__(type, brand, model, year, color, fuel)
        self.doors = doors

    def price(self):
        return 5000 + (500 * self.doors)

    def __str__(self):
        return f"{super().__str__()}, Puertas: {self.doors}, Precio: ${self.price()}"


class Truck(Vehicle):
    def __init__(self, type, brand, model, year, color, fuel, load_capacity):
        super().__init__(type, brand, model, year, color, fuel)
        self.load_capacity = load_capacity
    
    def price(self):
        return 10000 + (1000 * self.load_capacity)

    def __str__(self):
        return f"{super().__str__()}, Capacidad de carga: {self.load_capacity} toneladas, Precio: ${self.price()}"
    

class Filters(ABC):
    @abstractmethod
    def preguntarFiltro(self):
        pass

    @abstractmethod
    def mostrarResultado(self, vehicle):
        pass

class YearFilter(Filters):
    def __init__(self):
        self.pregunta = None
    def preguntarFiltro(self):
        self.pregunta = int(input("INGRESE AL AÑO MINIMO DE FABRICACION: "))
    def mostrarResultado(self, vehicle):
        return self.pregunta <= vehicle.year

class FuelTypeFilter(Filters):
    def __init__(self):
        self.pregunta = None
    def preguntarFiltro(self):
        self.pregunta = input("INGRESE EL TIPO DE COMBUSTIBLE: ")
    def mostrarResultado(self, vehicle):
        return self.pregunta.lower() == vehicle.fuel.lower()

class PriceFilter(Filters):
    def __init__(self):
        self.pregunta = None
    def preguntarFiltro(self):
        pass
    def mostrarResultado(self, vehicle):
        pass

class TypeVehicle:
    def __init__(self):
        self.pregunta = None
    def preguntarFiltro(self):
        self.pregunta = input("INGRESE EL TIPO DE VEHICULO QUE BUSCA: ")
    def mostrarResultado(self, vehicle):
        return self.pregunta.lower() == vehicle.type.lower()

class Store:
    def __init__(self):
        self.vehicles = []
    def load_json(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            for item in data:
                if item["type"] == "Car":
                    car = Car(item["type"],
                        item["brand"],
                        item["model"],
                        item["year"],
                        item["color"],
                        item["fuel"],
                        item["doors"])
                    self.vehicles.append(car)

                elif item["type"] == "Truck":
                    truck = Truck(item["type"],
                        item["brand"],
                        item["model"],
                        item["year"],
                        item["color"],
                        item["fuel"],
                        item["load_capacity"])
                    self.vehicles.append(truck)

    def start(self):
        while True:
            print("\nSeleccione un filtro para aplicar:")
            print("1. Filtro por Año de Fabricación")
            print("2. Filtro por Tipo de Combustible")
            print("3. Filtro por Precio")
            print("4. Filtro de Tipo de Vehiculo")
            print("0. Salir")

            choice = int(input("Ingrese su elección: "))
            if choice == 0:
                break

            if choice == 1:
                filter_instance = YearFilter()
            elif choice == 2:
                filter_instance = FuelTypeFilter()
            elif choice == 3:
                filter_instance = PriceFilter()
            elif choice == 4:
                filter_instance = TypeVehicle()
            else:
                print("Opción no válida, por favor intente de nuevo.")
                continue
            
            filter_instance.preguntarFiltro()
            filtered_vehicles = []
            for v in self.vehicles:
                if filter_instance.mostrarResultado(v):
                    filtered_vehicles.append(v)

            print("\nVehículos filtrados:")
            for vehicle in filtered_vehicles:
                print(f"{vehicle} - Precio: {vehicle.price()}")
store = Store()
store.load_json('/Users/martinrodriguez/PDP-2024-2/vehiclesPOO/vehicle.json')
store.start()


        