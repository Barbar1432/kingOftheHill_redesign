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
transposition_table = {}

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
        self.isMax = True
        self.can_castle_white_left = True
        self.can_castle_white_right = True
        self.can_castle_black_left = True
        self.can_castle_black_right = True
        self.move_generator = moveGenerator()
        self.king_reached_the_hill = False

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

    def move_piece(self, sqSelected, sqDest, chessBoard):
        from_row, from_col = sqSelected
        to_row, to_col = sqDest
        if self.isMax:
            positions = np.where(chessBoard > 0)
            move_dict = self.move_generator.legalMoves(chessBoard, positions, self.isMax, self.can_castle_white_right,
                                                       self.can_castle_white_left)
        if self.isMax == False:
            positions = np.where(chessBoard < 0)
            move_dict = self.move_generator.legalMoves(chessBoard, positions, self.isMax, self.can_castle_black_right,
                                                       self.can_castle_black_left)
        if (self.isMax and chessBoard[from_row][from_col] <= 0) or (
                not self.isMax and chessBoard[from_row][from_col] >= 0):
            # print ("invalid  move")
            return

        if move_dict[sqSelected].__contains__(sqDest):
            piece_value = chessBoard[from_row][from_col]
            chessBoard[to_row][to_col] = piece_value
            chessBoard[from_row][from_col] = 0
            # King reached the hill - Game Over:
            if self.isMax and piece_value == 2000:
                if sqDest in ((4, 3), (3, 3), (3, 4), (4, 4)):
                    self.king_reached_the_hill = True
            if not self.isMax and piece_value == -2000:
                if sqDest in ((4, 3), (3, 3), (3, 4), (4, 4)):
                    self.king_reached_the_hill = True
            self.isMax = not self.isMax
            self.castle_move(sqSelected, sqDest)

    def castle_move(self, sqSelected, sqDest):
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
                self.chessBoard[0][5] = -500
                self.chessBoard[0][7] = 0
            if sqSelected == (0, 4) or sqSelected == (0, 7):
                self.can_castle_black_right = False
        if self.can_castle_black_left:
            if (sqSelected == (0, 4) and sqDest == (0, 2)):
                self.chessBoard[0][3] = -500
                self.chessBoard[0][0] = 0
            if sqSelected == (0, 4) or sqSelected == (0, 0):
                self.can_castle_black_left = False

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
                child_node_list.append((key, value))  # Store the move and resulting board
        return child_node_list

    def bot_plays(self):
        _, path = alpha_beta(self, 3, float("-inf"), float("inf"), self.isMax)
        #print(k)
        if path is None or len(path) == 0:
            print("Game Over")
            return -1
        move = path[0]
        sqSelected, sqDest = move
        # print(sqSelected)

        self.move_piece(sqSelected, sqDest, self.chessBoard)
        return sqSelected, sqDest

    def move_piece_alphabeta(self, sqSelected, sqDest, chessBoard, isMax):
        from_row, from_col = sqSelected
        to_row, to_col = sqDest
        if isMax:
            positions = np.where(chessBoard > 0)
            move_dict = self.move_generator.legalMoves(chessBoard, positions, isMax, self.can_castle_white_right,
                                                       self.can_castle_white_left)
        if isMax == False:
            positions = np.where(chessBoard < 0)
            move_dict = self.move_generator.legalMoves(chessBoard, positions, isMax, self.can_castle_black_right,
                                                       self.can_castle_black_left)
        if (isMax and chessBoard[from_row][from_col] <= 0) or (not isMax and chessBoard[from_row][from_col] >= 0):
            # print ("invalid  move")
            return

        if move_dict[sqSelected].__contains__(sqDest):
            piece_value = chessBoard[from_row][from_col]
            chessBoard[to_row][to_col] = piece_value
            chessBoard[from_row][from_col] = 0
            # King reached the hill - Game Over:
            if self.isMax and piece_value == 2000:
                if sqDest in ((4, 3), (3, 3), (3, 4), (4, 4)):
                    self.king_reached_the_hill = True
            if not self.isMax and piece_value == -2000:
                if sqDest in ((4, 3), (3, 3), (3, 4), (4, 4)):
                    self.king_reached_the_hill = True
            self.isMax = not self.isMax
            self.castle_move(sqSelected, sqDest)
        # print(self.evaluation(self.chessBoard))

    def undo_move_alphabeta(self, selected, dest, old_selected_piece, old_dest_piece, old_b, old_w):
        row, col = selected
        row_d, col_d = dest
        self.chessBoard[row][col] = old_selected_piece
        self.chessBoard[row_d][col_d] = old_dest_piece
        self.isMax = not self.isMax

        if old_selected_piece == 2000 and dest in ((4, 3), (3, 3), (3, 4), (4, 4)):
            self.king_reached_the_hill = False
        if old_selected_piece == -2000 and dest in ((4, 3), (3, 3), (3, 4), (4, 4)):
            self.king_reached_the_hill = False

        # Last Move was a castling undo castle movement
        if old_b[0] != self.can_castle_black_right:
            if old_selected_piece == -2000 and dest == (0, 6):
                print("Undo castling")
                self.chessBoard[0][5] = 0
                self.chessBoard[0][7] = -500
            self.can_castle_black_right = True
        elif old_b[1] != self.can_castle_black_left:
            if old_selected_piece == -2000 and dest == (0, 2):
                print("Undo castling")
                self.chessBoard[0][3] = 0
                self.chessBoard[0][0] = -500
            self.can_castle_black_left = True
        elif old_w[0] != self.can_castle_white_right:
            if old_selected_piece == 2000 and dest == (7, 6):
                print("Undo castling")
                self.chessBoard[7][5] = 0
                self.chessBoard[7][7] = 500
            self.can_castle_white_right = True
        elif old_w[1] != self.can_castle_white_left:
            if old_selected_piece == 2000 and dest == (7, 2):
                print("Undo castling")
                self.chessBoard[7][3] = 0
                self.chessBoard[7][0] = 500
            self.can_castle_white_left = True




def alpha_beta(board, depth, alpha, beta, is_max, path=[]):
    if depth == 0 or board.king_reached_the_hill or is_game_Over(board):
        return evaluation(board.chessBoard), path

    hash_key = board_hash(board.chessBoard)

    if hash_key in transposition_table:
        entry = transposition_table[hash_key]
        if entry['depth'] >= depth:
            if entry['flag'] == 'exact':
                return entry['value'], entry['path']
            elif entry['flag'] == 'lowerbound' and entry['value'] > alpha:
                alpha = entry['value']
            elif entry['flag'] == 'upperbound' and entry['value'] < beta:
                beta = entry['value']
            if alpha >= beta:
                return entry['value'], entry['path']

    if is_max:
        best_value = alpha
        best_path = None
        for child_move, child_value, in board.generate_child_node(board.chessBoard):
            old_dest_piece = board.chessBoard[child_value[0]][child_value[1]]
            old_selec_piece = board.chessBoard[child_move[0]][child_move[1]]
            old_castling_w = (board.can_castle_white_right, board.can_castle_white_left)
            old_castling_b = (board.can_castle_black_right, board.can_castle_black_left)
            board.move_piece_alphabeta(child_move, child_value, board.chessBoard,
                                       True)  # Update the board with the move
            value, child_path = alpha_beta(board, depth - 1, best_value, beta, False,
                                           path + [(child_move, child_value)])
            board.undo_move_alphabeta(child_move, child_value, old_selec_piece, old_dest_piece, old_castling_b,
                                      old_castling_w)
            if value > best_value:
                best_value = value
                best_path = child_path
            if best_value >= beta:  # Beta-Cutoff
                break

        if best_value <= alpha:
            flag = 'upperbound'
        elif best_value >= beta:
            flag = 'lowerbound'
        else:
            flag = 'exact'
        transposition_table[hash_key] = {'value': best_value, 'flag': flag, 'depth': depth, 'path': best_path}
        return best_value, best_path
    else:
        best_value = beta
        best_path = None
        for child_move, child_value in board.generate_child_node(board.chessBoard):
            old_dest_piece = board.chessBoard[child_value[0]][child_value[1]]
            old_selec_piece = board.chessBoard[child_move[0]][child_move[1]]
            old_castling_w = (board.can_castle_white_right, board.can_castle_white_left)
            old_castling_b = (board.can_castle_black_right, board.can_castle_black_left)

            board.move_piece_alphabeta(child_move, child_value, board.chessBoard,
                                       False)  # Update the board with the move
            value, child_path = alpha_beta(board, depth - 1, alpha, best_value, True,
                                           path + [(child_move, child_value)])
            board.undo_move_alphabeta(child_move, child_value, old_selec_piece, old_dest_piece, old_castling_b,
                                      old_castling_w)
            if value < best_value:
                best_value = value
                best_path = child_path
            if best_value <= alpha:  # Alpha-Cutoff
                break

        if best_value <= alpha:
            flag = 'upperbound'
        elif best_value >= beta:
            flag = 'lowerbound'
        else:
            flag = 'exact'
        transposition_table[hash_key] = {'value': best_value, 'flag': flag, 'depth': depth, 'path': best_path}

        return best_value, best_path


# For Benchmark tests - Counting how many boards are visited
def alpha_beta_count(board, depth, alpha, beta, is_max, k=0, path=[]):
    k += 1
    if depth == 0 or board.king_reached_the_hill or is_game_Over(board):
        return evaluation(board.chessBoard), path, k


    if is_max:
        best_value = alpha
        best_path = None
        for child_move, child_value, in board.generate_child_node(board.chessBoard):
            old_dest_piece = board.chessBoard[child_value[0]][child_value[1]]
            old_selec_piece = board.chessBoard[child_move[0]][child_move[1]]
            old_castling_w = (board.can_castle_white_right, board.can_castle_white_left)
            old_castling_b = (board.can_castle_black_right, board.can_castle_black_left)
            board.move_piece_alphabeta(child_move, child_value, board.chessBoard,
                                       True)  # Update the board with the move
            value, child_path, k = alpha_beta_count(board, depth - 1, best_value, beta, False, k,
                                                    path + [(child_move, child_value)])
            board.undo_move_alphabeta(child_move, child_value, old_selec_piece, old_dest_piece, old_castling_b,
                                      old_castling_w)
            if value > best_value:
                best_value = value
                best_path = child_path
            if best_value >= beta:  # Beta-Cutoff
                break


        return best_value, best_path, k
    else:
        best_value = beta
        best_path = None
        for child_move, child_value in board.generate_child_node(board.chessBoard):
            old_dest_piece = board.chessBoard[child_value[0]][child_value[1]]
            old_selec_piece = board.chessBoard[child_move[0]][child_move[1]]
            old_castling_w = (board.can_castle_white_right, board.can_castle_white_left)
            old_castling_b = (board.can_castle_black_right, board.can_castle_black_left)

            board.move_piece_alphabeta(child_move, child_value, board.chessBoard,
                                       False)  # Update the board with the move
            value, child_path, k = alpha_beta_count(board, depth - 1, alpha, best_value, True, k,
                                                    path + [(child_move, child_value)])
            board.undo_move_alphabeta(child_move, child_value, old_selec_piece, old_dest_piece, old_castling_b,
                                      old_castling_w)
            if value < best_value:
                best_value = value
                best_path = child_path
            if best_value <= alpha:  # Alpha-Cutoff
                break


        return best_value, best_path, k

def board_hash(board):
    hash = 0
    for row in range(8):
        for col in range(8):
            if board[row][col] != 0:
                piece = board[row][col]
                position_of_board = (row) * 8 + (col + 1)
                hash += (piece * position_of_board)
    return hash


def evaluation(board):
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


def is_game_Over(board):
    if board.isMax:
        positions = np.where(board.chessBoard > 0)
        can_castle_left = board.can_castle_white_left
        can_castle_right = board.can_castle_white_right
        moves = board.move_generator.legalMoves(board.chessBoard, positions, board.isMax, can_castle_right,
                                                can_castle_left)
        if len(moves) == 0:
            print("There are no more possible moves.")
            return 1
    else:
        positions = np.where(board.chessBoard < 0)
        can_castle_left = board.can_castle_black_left
        can_castle_right = board.can_castle_black_right
        moves = board.move_generator.legalMoves(board.chessBoard, positions, board.isMax, can_castle_right,
                                                can_castle_left)
        if len(moves) == 0:
            print("There are no more possible moves.")
            return 1
    return 0


###### Old alpha beta #######
"""
    def alpha_beta(self, node, depth, alpha, beta, is_max, path=[]):
        if depth == 0:
            return self.evaluation(node), path
        if is_max:
            best_value = alpha
            best_path = None
            for child_move, child_value, in self.generate_child_node(node):
                child_board = np.copy(node)
                self.move_piece_alphabeta(child_move, child_value, child_board, True)  # Update the board with the move
                value, child_path = self.alpha_beta(child_board, depth - 1, best_value, beta, False,
                                                    path + [(child_move, child_value)])
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
                self.move_piece_alphabeta(child_move, child_value, child_board, False)  # Update the board with the move
                value, child_path = self.alpha_beta(child_board, depth - 1, alpha, best_value, True,
                                                    path + [(child_move, child_value)])
                if value < best_value:
                    best_value = value
                    best_path = child_path
                if best_value <= alpha:  # Alpha-Cutoff
                    break
            return best_value, best_path
"""


















