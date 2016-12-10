from model.class_pawn import Pawn
from model.class_pawn import *
from model.class_board_game import *

board = Board()
board.show()
board.cases[0] =  Pawn("Reine", "blanc")

print("\nTest afficher nom\n\n")
board.showCase(0)
