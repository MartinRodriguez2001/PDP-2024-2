from abc import ABC, abstractmethod
from typing import List
from typing import List, Optional
from typing import List
import json
from typing import List, Type

class Furniture(ABC):
  def __init__(self, model: str, width: int, height: int,
               depth: int, colors: List[str], spaces: List[str]) -> None:
    self._model: str = model
    self._width: int = width
    self._height: int = height
    self._depth: int = depth
    self._colors: List[str] = colors
    self._spaces: List[str] = spaces

  @property
  def volume(self) -> int:
    return self._width * self._height * self._depth

  @property
  @abstractmethod
  def price(self) -> int:
    ...

  @property
  def shipping_factor(self) -> float:
    return min(max(1, self.volume/200000), 5)

  def has_color(self, color: str) -> bool:
    return color in self._colors

  def __str__(self) -> str:
    return f'{self.__class__.__name__}: {self._model} ({self._width}x{self._height}x{self._depth}) - ${self.price} (x{self.shipping_factor})'

class Nightstand(Furniture):
  def __init__(self, model: str, width: int, height: int,
               depth: int, colors: List[str], spaces: List[str],
               material: str) -> None:
    super().__init__(model, width, height, depth, colors, spaces)
    self._material: str = material

  @property
  def price(self) -> int:
    return 40 + (0 if self._material != "wood" else 30)

class Cupboard(Furniture):
  def __init__(self, model: str, width: int, height: int,
               depth: int, colors: List[str], spaces: List[str],
               doors_count: int, doors_material: Optional[str] = None) -> None:
    super().__init__(model, width, height, depth, colors, spaces)
    self._doors_count: int = doors_count
    self._doors_material: Optional[str] = doors_material

  @property
  def price(self) -> int:
    return 80 + 5*self._doors_count*(1 if self._doors_material != "glass" else 2)
  
class DinningSet(Furniture):
    def __init__(self, model: str, width: int, height: int, 
                 depth: int, colors: List[str], spaces: List[str], seating: int):
      super().__init__(model, width, height, depth, colors, spaces)
      self._seating: int = seating

    @property
    def price(self) -> int:
      return 100 + (10 * self._seating)

#----------------------------------------------------------------------------

class FurnitureFilter(ABC):
    @abstractmethod
    def filtroBuscado(self, furniture):
        pass
    def preguntarFiltro(self):
        pass
    def mostrarResultado(self):
        pass

class ColorFilter(FurnitureFilter):
    def __init__(self):
      self.pregunta = None
    def filtroBuscado(self, furniture):
       return self.color in furniture.colors
    def preguntarFiltro(self):
       self.pregunta = input("INGRESE EL FILTRO QUE DESEA APLICAR")
    def mostrarResultado(self):
       print(f"filtro de color: {self.color}")



class Store:
  def __init__(self) -> None:
    self._furnitures: List[Furniture] = []

  def load_furnitures(self, filename: str) -> None:
    with open(filename, 'r') as f:
        data = json.load(f)

        for fur in data:
            class_name = fur.pop("type")
            if class_name in globals():
                self._furnitures.append(globals()[class_name](**fur))

  def load_filters(self) -> None:
    ...

  def start(self) -> None:
    # Ud. deben implementarlo
    ...

  def show_furnitures(self) -> None:
    self._show_furnitures(self._furnitures)

  def _show_furnitures(self, f_list: List[Furniture]) -> None:
    for f in f_list:
        print(f)


s = Store()
s.load_furnitures('/Users/martinrodriguez/PDP-2024-2/mueblesLab2_2024_10/muebles01.json')
s.load_filters()
s.show_furnitures()
s.start()