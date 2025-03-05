from player import humanPlayer, computerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.currentWinner = None
    
    def printBoard(self):
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")
    
    def printBoardNums(self):
        boardNum = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in boardNum:
            print("| " + " | ".join(row) + " |")

            
    def availMoves(self):
        # moves = []
        # for (i, x) in enumerate(self.board):
        #     if x == " ":
        #         moves.append(i)
        # return moves
        
        return [i for i, x in enumerate(self.board) if x == " "]
    
    def emptySquare(self):
        return " " in self.board
    
    def numEmpty(self):
        return self.board.count(" ")
    
    def makeMove(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.currentWinner = letter
            return True
        else: return False
        
    def winner(self, square, letter):
        row_ind = square % 3 
        row = self.board[row_ind*3 : (row_ind+1)*3] 
        if all([spot == letter for spot in row]):
            return True
        
        col_ind = square % 3
        col = self.board[col_ind*3 : (col_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                    return True
            
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                    return True
        return False
    
def play(game, x, o, print_game = True):
    if print_game:
        game.printBoardNums()
        
    letter = "x"
    
    while game.emptySquare():
        if letter == "o": square = o.getMove(game)
        else: square = x.getMove(game)
    
        if game.makeMove(square, letter):
            if print_game:
                print(letter + " make a move to square " + str(square))
                game.printBoard()
                print("")
                
            if game.currentWinner:
                if print_game:
                    print(letter + " is the winner")
                return letter
            
            letter = "o" if letter == "x" else "x"
        
    if print_game: print("It's a tie")
    
if __name__ == "__main__":
    x = humanPlayer("x")
    o = computerPlayer("o")
    
    t = TicTacToe()
    play(t, x, o, print_game=True)