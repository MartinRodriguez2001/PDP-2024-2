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

class Car(Vehicle):
    def __init__(self, type, brand, model, year, color, fuel, doors):
        super().__init__(type, brand, model, year, color, fuel)
        self.doors = doors

    def price(self):
        return 5000 + (500 * self.doors)

class Truck(Vehicle):
    def __init__(self, type, brand, model, year, color, fuel, load_capacity):
        super().__init__(type, brand, model, year, color, fuel)
        self.load_capacity = load_capacity
    
    def price(self):
        return 10000 + (1000 * self.load_capacity)
    

class Filters(ABC):
    @abstractmethod
    def filtroBuscado(self, furniture):
        pass
    @abstractmethod
    def preguntarFiltro(self):
        pass
    @abstractmethod
    def mostrarResultado(self):
        pass

class YearFilter(Filters):
    def __init__(self):
        self.pregunta = None
    def filtroBuscado(self):
        pass
    def pregunta(self):
        pass
    def mostrarResultado(self):
        pass

class FuelTypeFilter(Filters):
    def __init__(self):
        self.pregunta = None
    def filtroBuscado(self):
        pass
    def pregunta(self):
        pass
    def mostrarResultado(self):
        pass

class PriceFilter(Filters):
    def __init__(self):
        self.pregunta = None
    def filtroBuscado(self):
        pass
    def pregunta(self):
        pass
    def mostrarResultado(self):
        pass

class Store:
    def __init__(self):
        self.opcion = None
    def load_json(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)

        