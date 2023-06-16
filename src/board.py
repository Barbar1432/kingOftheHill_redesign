import numpy as np
import pygame
from moveGenerator import moveGenerator

# Constants for colors, screen size, and square size
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
SQUARE_SIZE = 60
DARK_GREEN = (79, 121, 66)
LIGHT_GREEN = (158, 194, 133)

class Board:
    def __init__(self):
        # Create the chess board
        self.chessBoard = np.array([
            [-500, -320, -330, -900, -2000, -330, -320, -500],
            [-100 for _ in range(8)],
            [0 for _ in range(8)],
            [0 for _ in range(8)],
            [0 for _ in range(8)],
            [0 for _ in range(8)],
            [100 for _ in range(8)],
            [500, 320, 330, 900, 2000, 330, 320, 500]
        ])
        self.isMax=True
        self.can_castle_white_left= True
        self.can_castle_white_right = True
        self.can_castle_black_left =True
        self.can_castle_black_right = True

    def draw_board(self, screen):
        for row in range(8):
            for col in range(8):
                x = col * SQUARE_SIZE
                y = row * SQUARE_SIZE
                color = LIGHT_GREEN if (row + col) % 2 == 0 else DARK_GREEN
                pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))
                # Get the piece value from the chess board
                piece_value = self.chessBoard[row][col]
                # If there is a piece on the current square, load the corresponding image
                if piece_value != 0:
                    piece_image = pygame.image.load(f"{piece_value}.png")
                    screen.blit(piece_image, (x, y))

    def move_piece(self, sqSelected,sqDest):
        from_row, from_col = sqSelected
        to_row, to_col  =sqDest
        move_generator = moveGenerator()
        if self.isMax :
         positions = np.where (self.chessBoard>0)
         move_dict = move_generator.legalMoves(self.chessBoard, positions, self.isMax,self.can_castle_white_right,self.can_castle_white_left )
        if self.isMax== False:
            positions = np.where(self.chessBoard < 0)
            move_dict = move_generator.legalMoves(self.chessBoard, positions, self.isMax, self.can_castle_black_right,self.can_castle_black_left)
        if (self.isMax and self.chessBoard[from_row][from_col] <= 0) or (not self.isMax and self.chessBoard[from_row][from_col] >= 0):
            print("Invalid move. It's not your turn.")
            return
        print(move_dict[sqSelected])
        if  move_dict[sqSelected].__contains__(sqDest):
           piece_value = self.chessBoard[from_row][from_col]
           self.chessBoard[to_row][to_col] = piece_value
           self.chessBoard[from_row][from_col] = 0
           self.isMax = not self.isMax
           self.castle_move(sqSelected,sqDest)


            

    def castle_move(self,sqSelected,sqDest):
        if self.can_castle_white_right:
            if (sqSelected == (7, 4) and sqDest == (7, 6)):
                self.chessBoard[7][5] = 500
                self.chessBoard[7][7] = 0
            if sqSelected == (7, 4) or sqSelected == (7, 7):
                self.can_castle_white_right = False

        if self.can_castle_white_left:
            if (sqSelected == (7, 4) and sqDest == (7, 2)):
                self.chessBoard[7][3] = 500
                self.chessBoard[7][0] = 0

            if sqSelected == (7, 4) or sqSelected == (7, 0):
                self.can_castle_white_left = False

        if self.can_castle_black_right:
            if (sqSelected == (0, 4) and sqDest == (0, 6)):
                self.chessBoard[0][5] = 500
                self.chessBoard[0][7] = 0
            if sqSelected == (0, 4) or sqSelected == (0, 7):
                self.can_castle_black_right = False
        if self.can_castle_black_left:
            if (sqSelected == (0, 4) and sqDest == (0, 2)):
                self.chessBoard[0][3] = 500
                self.chessBoard[0][0] = 0
            if sqSelected == (0, 4) or sqSelected == (0, 0):
                self.can_castle_black_right = False








