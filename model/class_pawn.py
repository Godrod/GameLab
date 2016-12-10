from enum import Enum

class TypePawn(Enum):
    dame = 1
    roi = 2
    pion = 3
    cavalier = 4
    tour = 5
    fou = 6
class TypeColor(Enum):
    noir = 1
    blanc = 2
class TypeLife(Enum):
    vivant = 1
    mort = 2

class Pawn(object):
    def __init__(self, nom, couleur):
        self.nom = nom
        self.couleur = couleur
        

    def deplacement(self):
        print (str(self.nom))
