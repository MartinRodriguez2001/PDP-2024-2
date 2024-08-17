import random

class RobotType:
    def __init__(self, name):
        self.name = name
        self.strengths = []
        self.weaknesses = []
    
    def add_strength(self, rtype):
        self.strengths.append(rtype)
    
    def add_weakness(self, rtype):
        self.weaknesses.append(rtype)
    
    def type_factor(self, rtype): #multiplicador dependiendo de contra quien se está enfrentando un robot
        if rtype in self.strengths:
            return 1.5
        elif rtype in self.weaknesses:
            return 0.5
        else:
            return 1.0
        
#prueba de funcionamiento de la clase robotType
#steel = RobotType("Steel")
#plastic = RobotType("Plastic")
#electric = RobotType("Electric")

#steel.add_strength(plastic)
#steel.add_weakness(electric)

#print(steel.type_factor(plastic))
#print(steel.type_factor(electric))
#print(steel.type_factor(steel)) 

class Move:
    def __init__(self, name, rtype, attack, defense):
        self.name = name
        self.rtype = rtype #intancia de robotType
        self.attack = attack
        self.defense = defense
    
    def get_name(self):
        return self.name
    
    def get_rtype(self):
        return self.rtype
    
    def get_attack(self):
        return self.attack
    
    def get_defense(self):
        return self.defense
#prueba de funcionamiento de la clase move
#steel = RobotType("Steel")
#metal_punch = Move("Metal Punch", steel, 30, 10)

#print(metal_punch.get_name())
#print(metal_punch.get_rtype().name)
#print(metal_punch.get_attack())
#print(metal_punch.get_defense())

class Robot:
    def __init__(self, name, rtype, energy, defense):
        self.name = name
        self.rtype = rtype #intancia de RobotType
        self.energy = energy
        self.defense = defense
        self.moves = []
    
    def get_name(self):
        return self.name
    
    def get_rtype(self):
        return self.rtype

    def get_energy(self):
        return self.energy
    
    def get_defense(self):
        return self.defense

    def add_move(self, move):
        self.moves.append(move)

    def random_move(self):
        return random.choice(self.moves)

#prueba de funcionamiento de clase robot
#steel = RobotType("Steel")
#metal_punch = Move("Metal Punch", steel, 30, 10)
#robo_steel = Robot("RoboSteel", steel, 100, 20)

#robo_steel.add_move(metal_punch)

#print(robo_steel.get_name())
#print(robo_steel.get_rtype().name)
#print(robo_steel.get_energy())
#print(robo_steel.random_move().get_name())

class Battle:
    def __init__(self, r1, r2):
        self.r1 = r1
        self.r2 = r2
    
    def load_robots(self, filename):
        pass

    def calculate_damage(self, move, defender):
        type_factor = move.get_rtype().type_factor(defender.get_rtype())
        damage = (move.get_attack() * type_factor) - defender.get_defense()
        return max(0, damage)  # Asegura que el daño no sea negativo
    
    def take_turn(self, attacker, defender):
        move = attacker.random_move()
        damage = self.calculate_damage(move, defender)
        defender.energy -= damage
        print(f"{attacker.get_name()} usa {move.get_name()} y causa {damage} de daño a {defender.get_name()}. Energía restante de {defender.get_name()}: {defender.get_energy()}")

    
    def start(self):
        pass

    def fight(self):
        print(f"¡Comienza la batalla entre {self.r1.get_name()} y {self.r2.get_name()}!")
        attacker, defender = self.r1, self.r2

        while self.r1.get_energy() > 0 and self.r2.get_energy() > 0:
            self.take_turn(attacker, defender)
            attacker, defender = defender, attacker  # Cambia de turno
            if self.r1.get_energy() > 0:
                print(f"¡{self.r1.get_name()} gana la batalla!")
            else:
                print(f"¡{self.r2.get_name()} gana la batalla!")

#prueba de funcionamiento de la clase battle
#teel = RobotType("Steel")
#plastic = RobotType("Plastic")

#metal_punch = Move("Metal Punch", steel, 30, 10)
#plastic_slam = Move("Plastic Slam", plastic, 25, 15)

#robo_steel = Robot("RoboSteel", steel, 100, 20)
#plastic_bot = Robot("PlasticBot", plastic, 100, 25)

#robo_steel.add_move(metal_punch)
#plastic_bot.add_move(plastic_slam)

#battle = Battle(robo_steel, plastic_bot)
#battle.fight()

