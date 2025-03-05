import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter
        
    def getMove(self, game):
        pass
    
class computerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def getMove(self, game):
        square = random.choice(game.availMoves())
        return square

class humanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def getMove(self, game):
        validSquare = False
        value = None
        while not validSquare:
            square = input(self.letter + "'s turn, Input move (0-9): ")
            try:
                val = int(square)
                if val not in game.availMoves():
                    raise ValueError
                validSquare = True
            except:
                print("Invalid square, try again")
            
        return val