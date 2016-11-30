from enum import Enum

class TypeBoard(Enum):
    case = 1
    casedepart = 2

class Board(object):
    def __init__(self):
        self.cases = range(0,64)

    def deplacement(self):
        print("le plateau se deplace")
