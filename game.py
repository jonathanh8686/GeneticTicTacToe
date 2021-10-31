from typing import ValuesView
from numba import jit

class Game(object):
    BOARD_SIZE = 3
    DEFAULT_LETTER = ' '
    O_LETTER = 'O'
    X_LETTER = 'X'

    def __init__(self):
        self.board = [[self.DEFAULT_LETTER for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        self.turn = self.X_LETTER
    
    def __repr__(self):
        rtn = ""
        for i in self.board:
            rtn += " | ".join(i) + "\n" + (self.BOARD_SIZE * "---") + "\n"
        return rtn
    
    def make_move(self, r, c):
        if(r < 0 or r >= self.BOARD_SIZE or c < 0 or c >= self.BOARD_SIZE):
            raise ValueError("Row and Column are out of range!")
        if(self.board[r][c] != self.DEFAULT_LETTER):
            raise ValueError("Cell has already been filled!")
        self.board[r][c] = self.turn
        self.turn = self.O_LETTER if self.turn == self.X_LETTER else self.X_LETTER
    
    def check_won(self):
        b = self.board
        for i in range(3):
            if(b[i][0] != " " and b[i][0] == b[i][1] and b[i][1] == b[i][2]):
                return b[i][0]
            if(b[0][i] != " " and b[0][i] == b[1][i] and b[1][i] == b[1][i]):
                return b[0][i]
        if(b[0][0] != " " and b[0][0] == b[1][1] and b[1][1] == b[2][2]):
            return b[0][0]
        if(b[0][2] != " " and b[0][2] == b[1][1] and b[1][1] == b[2][0]):
            return b[0][2]
        
        for i in range(3):
            for j in range(3):
                if(b[i][j] == " "):
                    return False
        return " "

        # for i in range(self.BOARD_SIZE):
        #     if(self.board[i][0] != self.DEFAULT_LETTER) and all([self.board[i][j] == self.board[i][0] for j in range(self.BOARD_SIZE)]):
        #         return self.board[i][0]
        #     if(self.board[0][i] != self.DEFAULT_LETTER and all([self.board[j][i] == self.board[0][i] for j in range(self.BOARD_SIZE)])):
        #         return self.board[0][i]
        # if(self.board[0][self.BOARD_SIZE-1] != self.DEFAULT_LETTER and all([self.board[i][self.BOARD_SIZE-i-1] == self.board[0][self.BOARD_SIZE-1] for i in range(self.BOARD_SIZE)])):
        #     return self.board[0][self.BOARD_SIZE - 1]
        # if(self.board[0][0] != self.DEFAULT_LETTER and all([self.board[i][i] == self.board[0][0] for i in range(self.BOARD_SIZE)])):
        #     return self.board[0][0]

        # if(all([self.DEFAULT_LETTER not in self.board[i] for i in range(self.BOARD_SIZE)])):
        #     return self.DEFAULT_LETTER
        
        # return False

    
    def in_progress(self):
        return not self.check_won()

    def get_turn(self):
        return self.turn
    
    def get_board(self):
        return self.board[:]
    
        
