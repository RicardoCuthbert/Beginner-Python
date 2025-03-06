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
    
class AIComputer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def getMove(self, game):
        if len(game.availMoves()) == 9 or 4 in game.availMoves():
            square = 4
        else:
            square = self.minimax(game, self.letter, -math.inf, math.inf)["position"]
        return square
    
    def minimax(self, state, player, alpha, beta):
        max_player = self.letter # The AI
        other_player = "o" if player == "x" else "x"
        
        if state.currentWinner == other_player:
            return {
                "position": None, 
                "score": 1 * (state.numEmpty() + 1) if other_player == max_player else -1 * (state.numEmpty() + 1)
            }
        elif not state.emptySquare():
            return {"position": None, "score": 0}
        
        if player == max_player:
            best = {"position": None, "score": -math.inf}
        else:
            best = {"position": None, "score": math.inf}
            
        for possible_move in state.availMoves():
            state.makeMove(possible_move, player)
            
            sim_score = self.minimax(state, other_player, alpha, beta)
            
            state.board[possible_move] = " "
            state.currentWinner = None
            
            sim_score["position"] = possible_move
            
            if "score" not in sim_score:
                sim_score["score"] = 0  # Default score if missing

            
            if player == max_player:
                if sim_score["score"] > best["score"]:
                    best = sim_score
                alpha = max(alpha, best["score"])
            else:
                if sim_score["score"] < best["score"]:
                    best = sim_score
                beta = min(beta, best["score"])
                
            if beta <= alpha: break
        return best