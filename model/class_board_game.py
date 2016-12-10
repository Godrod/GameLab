from enum import Enum

class TypeBoard(Enum):
    case = 1
    casedepart = 2

class Board(object):
    def __init__(self):
        self.cases = [[0, 0, 0, 0, 0, 0, 0, 0], \
                      [0, 0, 0, 0, 0, 0, 0, 0], \
                      [0, 0, 0, 0, 0, 0, 0, 0], \
                      [0, 0, 0, 0, 0, 0, 0, 0], \
                      [0, 0, 0, 0, 0, 0, 0, 0], \
                      [0, 0, 0, 0, 0, 0, 0, 0], \
                      [0, 0, 0, 0, 0, 0, 0, 0]]


    def getBoard(self):
        return self.cases

    def show(self):
        i = 0
