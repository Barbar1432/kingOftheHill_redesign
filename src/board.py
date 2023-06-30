import numpy as np
import pygame
from moveGenerator import moveGenerator
from PST import PST
from evaluation import evaluation
from hash_board import hash_board

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
        self.eval = evaluation()
        self.last_move = None
        self.move_count = 0

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
            print("invalid  move")
            return

        if move_dict[sqSelected].__contains__(sqDest):
            piece_value = chessBoard[from_row][from_col]
            chessBoard[to_row][to_col] = piece_value
            chessBoard[from_row][from_col] = 0
            self.isMax = not self.isMax
            self.castle_move(sqSelected, sqDest)
            self.eval.board_evaluation(chessBoard,self.move_count)
            self.move_count+=1
            self.last_move = (sqSelected, sqDest)



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


    def generate_child_node(self, node,isMax):
        child_node_list = []
        if isMax:
            positions = np.where(node > 0)
            move_dict = self.move_generator.legalMoves(node, positions, isMax, self.can_castle_white_right,
                                                       self.can_castle_white_left)
        else:
            positions = np.where(node < 0)
            move_dict = self.move_generator.legalMoves(node, positions,isMax, self.can_castle_black_right,self.can_castle_black_left)
        for key, value_list in move_dict.items():
            for value in value_list:
                child_node_list.append((key, value))  # Store the move and resulting board

        child_node_list = self.move_sorting(child_node_list)
        """for x,y in child_node_list:
            if self.is_quite_move(x, y) == 0:
                print("ZAAA",0)
            else:

                print("ZAAA", 1)"""
        return child_node_list

    def move_sorting(self,list):
        middle_pos = {(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(3,5),(4,2),(4,3),(4,4),(4,5),(5,2),(5,3),(5,4),(5,5)}
        ordered_list = []
        count = 0
        for move, value in list:
            if self.is_quite_move(move,value) == 0:
                ordered_list.insert(0,(move,value))
                count += 1
            elif value in middle_pos:
                ordered_list.insert(count, (move, value))
            else:
                ordered_list.append((move,value))


        return ordered_list


    def is_quite_move(self, seq, dest):  # Check if the move is quite
        if self.chessBoard[dest[0]][dest[1]] != 0 or self.move_generator.is_king_threatened(seq, dest, self.isMax, self.chessBoard):
            #print(0, "ÇIKTIIII")
            return 0
        else:
            #print(1 ,"ÇIKTIIII")
            return 1

    def quite_search(self, node, depth, alpha, beta, is_max, path):  # Quiescence search
        if is_max:
            best_value = alpha
            best_path = None
            for child_move, child_value, in self.generate_child_node(node, is_max):
                if not self.is_quite_move(child_move, child_value):
                    child_board = np.copy(node)
                    self.move_piece_alphabeta(child_move, child_value, child_board,
                                              True)  # Update the board with the move
                    value = self.eval.board_evaluation(node, self.move_count)
                    child_path = [(child_move, child_value)]
                    if value > best_value:
                        best_value = value
                        best_path = path + child_path
                    if best_value >= beta:
                        break
            return best_value, best_path

        else:
            best_value = beta
            best_path = None
            for child_move, child_value, in self.generate_child_node(node, is_max):
                if not self.is_quite_move(child_move, child_value):
                    child_board = np.copy(node)
                    self.move_piece_alphabeta(child_move, child_value, child_board,
                                              True)  # Update the board with the move
                    value = self.eval.board_evaluation(node, self.move_count)
                    child_path = [(child_move, child_value)]
                    if value < best_value:
                        best_value = value
                        best_path = path + child_path
                    if best_value <= alpha:
                        break
            return best_value, best_path

    def alpha_beta(self, node, depth, alpha, beta, is_max, path=[]):
        originalAlpha = alpha

        hash_key = self.board_hash(node)
        if hash_key in transposition_table:

            entry = transposition_table[hash_key]
            if entry['depth'] >= depth:
                if entry['flag'] == 'exact':

                    return entry['value'], entry['path']

                elif entry['flag'] == 'lowerbound':
                    alpha = max(alpha, entry['value'])
                elif entry['flag'] == 'upperbound':
                    beta = min(beta, entry['value'])
                if alpha >= beta:
                    return entry['value'], entry['path']
        if self.gameOver(node, is_max):
            return self.eval.board_evaluation(node,self.move_count), path
        if depth == 0:
            # Quiescence search
            value, child_path = self.quite_search(node, depth, alpha, beta, is_max, path)
            return value, child_path
        if is_max:
            best_value = alpha
            best_path = None
            for child_move, child_value, in self.generate_child_node(node,is_max):
                child_board = np.copy(node)
                self.move_piece_alphabeta(child_move, child_value, child_board, True) # Update the board with the move

                value, child_path = self.alpha_beta(child_board, depth - 1, best_value, beta, False,path + [(child_move, child_value)])
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
            for child_move, child_value in self.generate_child_node(node,is_max):
                child_board = np.copy(node)
                self.move_piece_alphabeta(child_move, child_value, child_board, False)# Update the board with the move

                value, child_path = self.alpha_beta(child_board, depth - 1, alpha, best_value, True,
                                                    path + [(child_move, child_value)])
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

    def bot_plays(self):
        _, path = self.alpha_beta(self.chessBoard, 3, float("-inf"), float("inf"), self.isMax)
        # Game is over
        if path == [] or path is None:
            return -1
        move = path[0]
        sqSelected, sqDest = move

        self.move_piece(sqSelected, sqDest, self.chessBoard)
        self.move_count += 1
        return sqSelected, sqDest

    def board_hash(self, board):
        hashBoard = hash_board()

        result = 0
        for row in range(8):
            for col in range(8):
                if board[row][col] != 0:
                    piece = board[row][col]
                    position_of_board = (row) * 8 + (col + 1)
                    select_key = hashBoard.real_realhash[position_of_board]
                    result ^= select_key[piece]

        return result

    def move_piece_alphabeta(self, sqSelected, sqDest, chessBoard, isMax):
            from_row, from_col = sqSelected
            to_row, to_col = sqDest
            piece_value = chessBoard[from_row][from_col]
            chessBoard[to_row][to_col] = piece_value
            chessBoard[from_row][from_col] = 0
    def gameOver (self,board,isMax):
        central_squares = [(3, 3), (3, 4), (4, 3), (4, 4)]
        for pos in central_squares:
            r,c= pos
            if board[r][c]==2000 or  board[r][c]==-2000 :
                return True
        if isMax:
          positions = np.where(board > 0)
          moves = self.move_generator.legalMoves(board, positions, isMax, self.can_castle_white_right,
                                                 self.can_castle_white_left)
          if all(element == [] for element in list(moves.values())):
             return True
        else:
            positions = np.where(board < 0)
            moves = self.move_generator.legalMoves(board, positions, isMax, self.can_castle_white_right,
                                                   self.can_castle_white_left)
            if all(element == [] for element in list(moves.values())):
                return True
        return False










































