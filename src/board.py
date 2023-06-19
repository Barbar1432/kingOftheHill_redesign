import numpy as np
import pygame
from moveGenerator import moveGenerator
from PST import PST

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
        self.move_generator = moveGenerator()

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

    def move_piece(self, sqSelected,sqDest,chessBoard):
        from_row, from_col = sqSelected
        to_row, to_col  =sqDest
        if self.isMax :
         positions = np.where(chessBoard>0)
         move_dict = self.move_generator.legalMoves(chessBoard, positions, self.isMax,self.can_castle_white_right,self.can_castle_white_left )
        if self.isMax== False :
            positions = np.where(chessBoard < 0)
            move_dict = self.move_generator.legalMoves(chessBoard, positions, self.isMax, self.can_castle_black_right,self.can_castle_black_left)
        if (self.isMax and chessBoard[from_row][from_col] <= 0) or (not self.isMax and chessBoard[from_row][from_col] >= 0):
            print ("invalid  move")
            return

        if  move_dict[sqSelected].__contains__(sqDest):
           piece_value = chessBoard[from_row][from_col]
           chessBoard[to_row][to_col] = piece_value
           chessBoard[from_row][from_col] = 0
           self.isMax = not self.isMax
           self.castle_move(sqSelected,sqDest)
           print(self.evaluation(self.chessBoard))


            

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
                self.can_castle_black_left = False



    def evaluation(self, board):
        whitePoints = 0
        blackPoints = 0
        pst = PST()
        black_positions = np.where(board < 0)
        white_positions = np.where(board > 0)
        row_indices, col_indices = white_positions
        for row, col in zip(row_indices, col_indices):
            piece = board[row][col]
            whitePoints += piece
            table = pst.piece_tables[piece]
            whitePoints += table[row][col]
            if (piece == 100):
                temp = board[row + 1][col]
                if (temp == 100):
                    whitePoints = whitePoints - 10

        rindices, cindices = black_positions
        for r, c in zip(rindices, cindices):
            piece = board[r][c]
            blackPoints += abs(piece)
            table = pst.piece_tables[piece]
            blackPoints += table[r][c]
            if (piece == -100):
                temp = board[r + 1][c]
                if (temp == -100):
                    blackPoints = blackPoints - 10
        evaluation = (whitePoints - blackPoints)
        return evaluation

    def generate_child_node(self, node):
        child_node_list = []
        if self.isMax:
            positions = np.where(node > 0)
            move_dict = self.move_generator.legalMoves(node, positions, self.isMax, self.can_castle_white_right,
                                                       self.can_castle_white_left)
        else:
            positions = np.where(node < 0)
            move_dict = self.move_generator.legalMoves(node, positions, self.isMax, self.can_castle_black_right,
                                                       self.can_castle_black_left)

        for key, value_list in move_dict.items():
            for value in value_list:
                child_node_list.append((key, value) ) # Store the move and resulting board
        return child_node_list

    def alpha_beta(self, node, depth, alpha, beta, is_max, path=[]):
        if depth == 0:
            return self.evaluation(node), path
        if is_max:
            best_value = alpha
            best_path = None
            for child_move, child_value,  in self.generate_child_node(node):
                child_board = np.copy(node)
                self.move_piece_alphabeta(child_move, child_value, child_board,True)  # Update the board with the move
                value, child_path = self.alpha_beta(child_board, depth - 1, best_value, beta, False,
                                                    path + [(child_move,child_value)])
                if value > best_value:
                    best_value = value
                    best_path = child_path
                if best_value >= beta:  # Beta-Cutoff
                    break
            return best_value, best_path
        else:
            best_value = beta
            best_path = None
            for child_move, child_value in self.generate_child_node(node):
                child_board = np.copy(node)
                self.move_piece_alphabeta(child_move, child_value, child_board,False)  # Update the board with the move
                value, child_path = self.alpha_beta(child_board, depth - 1, alpha, best_value, True,
                                                    path + [(child_move,child_value)])
                if value < best_value:
                    best_value = value
                    best_path = child_path
                if best_value <= alpha:  # Alpha-Cutoff
                    break
            return best_value, best_path

    def bot_plays (self):
        _, path = self.alpha_beta(self.chessBoard, 2, float("-inf"), float("inf"), self.isMax)
        move = path[0]
        sqSelected,sqDest =move
        print(sqSelected)

        self.move_piece(sqSelected,sqDest,self.chessBoard)
        return sqSelected,sqDest

    def move_piece_alphabeta(self, sqSelected,sqDest,chessBoard,isMax):
        from_row, from_col = sqSelected
        to_row, to_col  =sqDest
        if isMax :
         positions = np.where(chessBoard>0)
         move_dict = self.move_generator.legalMoves(chessBoard, positions, isMax,self.can_castle_white_right,self.can_castle_white_left )
        if isMax== False :
            positions = np.where(chessBoard < 0)
            move_dict = self.move_generator.legalMoves(chessBoard, positions, isMax, self.can_castle_black_right,self.can_castle_black_left)
        if (isMax and chessBoard[from_row][from_col] <= 0) or (not isMax and chessBoard[from_row][from_col] >= 0):
            print ("invalid  move")
            return

        if  move_dict[sqSelected].__contains__(sqDest):
           piece_value = chessBoard[from_row][from_col]
           chessBoard[to_row][to_col] = piece_value
           chessBoard[from_row][from_col] = 0
           isMax = not isMax
           self.castle_move(sqSelected,sqDest)
           print(self.evaluation(self.chessBoard))
























