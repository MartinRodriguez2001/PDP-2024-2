import random

class TipoPersonaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.fortalezas = []
        self.debilidades = []
    
    def add_fortalezas(self, fortaleza):
        self.fortalezas.append(fortaleza)
    
    def add_debilidades(self, debilidad):
        self.debilidades.append(debilidad)

    def mostrar_info_tipo(self):
        return f"SOY UN {self.nombre.upper()} Y LES GANO FACILMENTE A: {self.fortalezas}, Y PIERDO CONTRA: {self.debilidades}"

    def factor_tipo(self, tipo):
        if tipo in self.fortalezas:
            return 1.5
        elif tipo in self.debilidades:
            return 0.5
        else: 
            return 1.0

class Movimientos:
    def __init__(self, nombre, tipo, attack, defense):
        self.nombre = nombre
        self.tipo = tipo 
        self.attack = attack
        self.defense = defense

    def get_nombre(self):
        return self.nombre
    
    def get_tipo(self):
        return self.tipo
    
    def get_attack(self):
        return self.attack
    
    def get_defense(self):
        return self.defense

class Personaje:
    def __init__(self, nombre, tipo, energia, defensa):
        self.nombre = nombre
        self.tipo = tipo
        self.energia = energia
        self.defensa = defensa
        self.movimientos = []
    
    def add_moves(self, move):
        self.movimientos.append(move)
    
    def random_move(self):
        return random.choice(self.movimientos)
    
    def get_tipo(self):
        return self.tipo

    def get_defense(self):
        return self.defensa
    
    def get_energia(self):
        return self.energia
    
    def get_name(self):
        return self.nombre
    
class Batalla:
    def __init__(self, p1, p2):
        self.p1 = p1 
        self.p2 = p2
    
    def calculador_daño(self, movimiento, defensor):
        factor_daño = movimiento.get_tipo().factor_tipo(defensor.get_tipo())
        daño = (movimiento.get_attack() * factor_daño) - defensor.get_defense()
        return max(0, daño)

    def turnos(self, atacante, defensor):
        move = atacante.random_move()
        daño = self.calculador_daño(move, defensor)
        defensor.energia -= daño
        print(f"{atacante.get_name().upper()} USA {move.get_nombre().upper()} EN {defensor.get_name().upper()}, QUITANDOLE {daño}. {defensor.get_name().upper()} TIENE {defensor.get_energia()} DE ENERGIA")

    def pelea(self):
        atacante, defensor = self.p1, self.p2
        while self.p1.get_energia() > 0 and self.p2.get_energia() > 0:
            self.turnos(atacante, defensor)
            atacante, defensor = defensor, atacante
            if self.p1.get_energia() > 0:
                print(f"EL GANADOR ES {self.p1.get_name().upper()}")
            else:
                print(f"EL GANADOR ES {self.p2.get_name().upper()}")

anime = TipoPersonaje("anime")
anime.add_fortalezas("liveAction")
anime.add_debilidades("manga")

manga = TipoPersonaje("liveAction")
manga.add_debilidades("anime")
manga.add_fortalezas("manga")

naruto = Personaje("naruto", anime, 100, 8)
goku = Personaje("goku", manga, 100, 7)

rasengan = Movimientos("rasengan", anime, 10, 3)
rasenshuriken = Movimientos("rasenshuriken", anime, 20, 2)

kamehameha = Movimientos("kamehameha", manga, 10, 3)

naruto.add_moves(rasengan)
naruto.add_moves(rasenshuriken)

goku.add_moves(kamehameha)

batalla1 = Batalla(naruto, goku)
batalla1.pelea()
