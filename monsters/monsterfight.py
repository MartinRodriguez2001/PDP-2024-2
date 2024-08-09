class MonsterType:
  def __init__(self, name):
    self.name = name
    self.strengths = []
    self.weaknesses = []

  def add_strength(self, mtype):
    self.strengths.append(mtype)

  def add_weakness(self, mtype):
    self.weaknesses.append(mtype)

  def type_factor(self, mtype):
    if mtype in self.strengths:
      return 1.5
    elif mtype in self.weaknesses:
      return 0.5
    else:
      return 1

class Move:
  def __init__(self, name, mtype, attack, defense):
    self.name = name
    self.mtype = mtype # mtype es de tipo MonsterType, no es un string con el nombre del tipo
    self.attack = attack
    self.defense = defense

  def get_name(self):
    return self.name

  def get_mtype(self):
    return self.mtype

  def get_attack(self):
    return self.attack

  def get_defense(self):
    return self.defense

import random

class Monster:
  def __init__(self, name, mtype, energy, defense):
    self.name = name
    self.mtype = mtype
    self.energy = energy
    self.defense = defense
    self.moves = []

  def get_name(self):
    return self.name

  def get_energy(self):
    return self.energy

  def add_move(self, move):
    self.moves.append(move)

  def random_move(self):
    return random.choice(self.moves)

import json

class Tournament:
  def __init__(self):
    self.monsters = []

  def load_monsters(self, filename):
    with open(filename, 'r') as f:
      data = json.load(f)
      mtypes = {}
      for mt in data['types']:
        mtypes[mt['name']] = MonsterType(mt['name'])

      for mt in data['types']:
        mtype = mtypes[mt['name']]
        if 'strengths' in mt:
          for ms in mt['strengths']:
            mtype.add_strength(mtypes[ms])
        if 'weakness' in mt:
          for mw in mt['weakness']:
            mtype.add_weakness(mtypes[mw])
      for mm in data['monsters']:
        monster = Monster(mm['name'],
                          mtypes[mm['type']],
                          mm['energy'],
                          mm['defense'])
        self.monsters.append(monster)

        for mv in mm['moves']:
          monster.add_move(Move(mv['name'],
                                mtypes[mv['type']],
                                mv['attack'],
                                mv['defense']))

  def start(self):
    for i in range(len(self.monsters)):
      m1 = self.monsters[i]
      for j in range(i+1, len(self.monsters)):
        m2 = self.monsters[j]
        self._fight(m1, m2)

  def _fight(self, m1, m2):
    print(f"Comenzando batalla: {m1.get_name()} vs {m2.get_name()}")
    m_current = m1
    while m1.get_energy() > 0 and m2.get_energy() > 0:
      move = m_current.random_move()

t = Tournament()
t.load_monsters('/Users/martinrodriguez/PDP-2024-2/monsters/monsters01.json')

t.start()