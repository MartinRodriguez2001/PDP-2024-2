class robot:
    def __init__(self,damage,precision,recharge):
        self.type = []
        self.objetive = []
        self.damage = damage
        self.precision = precision
        self.recharge = recharge

class RobotType:
    def __init__(self, name):
        self.name = name
        self.long = []
        self.sword = []
        self.hand = []

class RobotObjetive:
    def __init__(self):
        self.unique = []
        self.group = []