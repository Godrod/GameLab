from enum import Enum

class TypeBoard(Enum):
    case = 1
    casedepart = 2

class Board(object):
    def __init__(self):
        self.cases = [ 0, 0, 0, 0, 0, 0, 0, 0, \
                      0, 0, 0, 0, 0, 0, 0, 0, \
                      0, 0, 0, 0, 0, 0, 0, 0, \
                      0, 0, 0, 0, 0, 0, 0, 0, \
                      0, 0, 0, 0, 0, 0, 0, 0, \
                      0, 0, 0, 0, 0, 0, 0, 0, \
                      0, 0, 0, 0, 0, 0, 0, 0, \
                      0, 0, 0, 0, 0, 0, 0, 0 ]


    def getBoard(self):
        return self.cases

    def show(self):
        i = 0
        while(i < 63):
            print('|', self.cases[i], '|', self.cases[i+1], '|', self.cases[i+2], '|', self.cases[i+3], '|', self.cases[i+4], '|', self.cases[i+5], '|', self.cases[i+6], '|', self.cases[i+7], '|')
            i = i + 8

    def showCase(self, case):
        print('|', self.cases[case].nom,'|')
