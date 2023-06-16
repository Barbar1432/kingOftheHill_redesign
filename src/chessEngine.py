import numpy as np
import pygame
from moveGenerator import moveGenerator
from board import Board
from PST import PST
class chessEngine:
    def __init__(self):
        return


    def evaluation(self,board):
        whitePoints = 0
        blackPoints = 0
        pst = PST()
        black_positions = np.where(board < 0)
        white_positions = np.where(board > 0)
        row_indices, col_indices = white_positions
        for row, col in zip(row_indices, col_indices):
            piece = board[row][col]
            whitePoints+= piece
            table= pst.piece_tables[piece]
            whitePoints+= table[row][col]
            if (piece ==100):
                temp = board[row + 1][col]
                if (temp ==100):
                        whitePoints = whitePoints - 10

        rindices, cindices = black_positions
        for r, c in zip(rindices, cindices):
            piece = board[r][c]
            blackPoints += abs(piece)
            table = pst.piece_tables[piece]
            blackPoints += table[r][c]
            if (piece==-100):
                temp = self.board[r + 1][c]
                if (temp==-100):
                    blackPoints = blackPoints - 10
        bewertung = (whitePoints - blackPoints)
        return bewertung



        def isTerminal ():
            return


