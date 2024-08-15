from abc import ABC, abstractmethod
import json


class Producto:
    def __init__(self, type, brand, model, year, color, price):
        self.type = type
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price
    
    def __str__(self):
        return f"{self.type} - {self.brand} {self.model} {self.year} {self.color}"

class Smatphone(Producto):
    def __init__(self, type, brand, model, year, color, price, screen_size, battery_capacity):
        super().__init__(type, brand, model, year, color, price)
        self.screen_size = screen_size
        self.battery_capacity = battery_capacity

    def priceProduct(self):
        return self.price + 200

    def __str__(self):
        return f"{super().__str__()}, Screen_size: ${self.screen_size}, Battery_capacity: ${self.battery_capacity}, Precio: ${self.priceProduct()}"

class Laptop(Producto):
    def __init__(self, type, brand, model, year, color, price, ram, processor):
        super().__init__(type, brand, model, year, color, price)
        self.ram = ram
        self.processor = processor

    def priceProduct(self):
        return self.price + 500
    
    def __str__(self):
        return f"{super().__str__()}, RAM: ${self.ram}, Processor: ${self.processor}, Precio: ${self.priceProduct()}"

class Filters(ABC):
    @abstractmethod
    def preguntarFiltro(self):
        pass
    def CompararFiltro(self):
        pass

class ColorFilter(Filters):
    def __init__(self):
        self.colo = None
    def preguntarFiltro(self):
        self.color = input("INGRESE EL COLOR QUE ESTÁ BUSCADO: ")
    def CompararFiltro(self, producto):
        return self.color.lower() == producto.color.lower()

class PriceRangeFilter(Filters):
    def __init__(self):
        self.minPrice = None
        self.maxPrice = None
    def preguntarFiltro(self):
        self.minPrice = int(input("INGRESE EL VALOR MINIMO DE PRECIO: "))
        self.maxPrice = int(input("INGRESE EL VALOR MAXIMO DE PRECIO: "))
    def CompararFiltro(self, producto):
        return self.minPrice <= producto.priceProduct() <= self.maxPrice

class YearFilter(Filters):
    def __init__(self):
        self.año = None
    def preguntarFiltro(self):
        self.año = int(input("INGRESE EL AÑO QUE ESTA BUSCANDO: "))
    def CompararFiltro(self, producto):
        return producto.year >= self.año

class Store:
    def __init__(self):
        self.productos = []
    def load_json(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            for p in data:
                if p["type"] == "Smartphone":
                    smatphone = Smatphone(p["type"],
                                          p["brand"],
                                          p["model"],
                                          p["year"],
                                          p["color"],
                                          p["price"],
                                          p["screen_size"],
                                          p["battery_capacity"])
                    self.productos.append(smatphone)
                elif p["type"] == "Laptop":
                    laptop = Laptop(p["type"],
                                    p["brand"],
                                    p["model"],
                                    p["year"],
                                    p["color"],
                                    p["price"],
                                    p["ram"],
                                    p["processor"])
                    self.productos.append(laptop)
    def start(self):
        while True:
            print("INGRESE UNA DE LAS SIGUIENTES OPCIONES")
            print("1. AGREGAR FILTRO DE COLOR")
            print("2. AGREGAR FILTRO DE PRECIO")
            print("3. AGREGAR FILTRO DE AÑO")
            print("0. SALIR")

            opcion = int(input("INGRESE UN FILTRO PARA APLICAR: "))
            if opcion == 0:
                break
            if opcion == 1:
                instancia_filtro = ColorFilter()
            elif opcion == 2:
                instancia_filtro = PriceRangeFilter()
            elif opcion == 3:
                instancia_filtro = YearFilter()
            else:
                print("OPCION INVALIDA. INGRESE NUEVAMENTE UNA OPCION")
                continue
            instancia_filtro.preguntarFiltro()
            lista_filtrados = []
            for p in self.productos:
                if instancia_filtro.CompararFiltro(p):
                    lista_filtrados.append(p)
            print("\nProductos filtrados:")
            for p in lista_filtrados:
                print(f"{p} - Precio: {p.priceProduct()}")

store = Store()
store.load_json('/Users/martinrodriguez/PDP-2024-2/productosPOO/productos.json')
store.start()
                




