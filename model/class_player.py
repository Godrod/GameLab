from enum import Enum

class TypePlayer(Enum):
    player_one = 1
    player_two = 2

class Player(object):
    def __init__(self, nom, couleur, gagne,numero):
        self.nom = nom
        self.couleur = couleur
        self.gagne = gagne
        self.numero = numero
