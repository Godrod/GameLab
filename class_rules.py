from enum import Enum

class TypeRules(Enum):
    tour = 1
    regle = 2

class Rules(object):
    def __init__(self, nom):
        self.nom = nom

    def deplacement(self):
