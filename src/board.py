import numpy as np
import pygame
from moveGenerator import moveGenerator
from PST import PST
from evaluation import evaluation
from hash_board import hash_board
from bot import bot_play_monte_carlo


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
        self.move_count =0
        self.last_move = None
        self.selected_square = None
        self.white_hill_win = False
        self.black_hill_win = False
        # Text conditions - For dialogue choice
        self.last_condition = "greeting"
        self.urgency = True  # If its urgent cut the old sentence and load the urgent one first
        self.end_dialogue = False

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
            self.last_condition = "move_invalid"
            return

        if move_dict[sqSelected].__contains__(sqDest):
            # Move is capture move
            if chessBoard[to_row][to_col] > 0:  # Rearrange this when white bot availability is added!
                self.last_condition = "move_capture_queen"
            if chessBoard[to_row][to_col] < 0:  # Rearrange this when white bot availability is added!
                self.last_condition = "move_capture"
            # Move is king to the hill move
            if chessBoard[from_row][from_col] == -2000:
                if sqDest in ((3, 3), (3, 4), (4, 3), (4, 4)):
                    self.last_condition = "queen_reached_hill"
                    self.urgency = True
                    self.black_hill_win = True
            elif chessBoard[from_row][from_col] == 2000:
                if sqDest in ((3, 3), (3, 4), (4, 3), (4, 4)):
                    self.last_condition = "hill_reached"
                    self.urgency = True
                    self.white_hill_win = True
            piece_value = chessBoard[from_row][from_col]
            chessBoard[to_row][to_col] = piece_value
            chessBoard[from_row][from_col] = 0

            # Move is check move
            if self.isMax:  # White Turn
                king = np.where(self.chessBoard == -2000)
                if self.move_generator.get_possible_moves(self.chessBoard, sqDest).__contains__(king):
                    print("Move check queen")
                    self.last_condition = "move_check_queen"
                    self.urgency = True
            else:
                king = np.where(self.chessBoard == 2000)
                if self.move_generator.get_possible_moves(self.chessBoard, sqDest).__contains__(king):
                    print("Move check")
                    self.last_condition = "move_check"
                    self.urgency = True

            self.isMax = not self.isMax
            self.castle_move(sqSelected, sqDest)
            self.move_count += 1
            self.last_move = (sqSelected, sqDest)
        else:
            if sqSelected != sqDest:
                self.last_condition = "move_invalid"
                self.urgency = True

    def zugsortierung(self, node, isMax):
        child_node_list = []
        if isMax:
            positions = np.where(node > 0)
            move_dict = self.move_generator.legalMoves(node, positions, isMax, self.can_castle_white_right,
                                                       self.can_castle_white_left)
        else:
            positions = np.where(node < 0)
            move_dict = self.move_generator.legalMoves(node, positions, isMax, self.can_castle_black_right,
                                                       self.can_castle_black_left)
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

    def move_sorting(self, list):
        middle_pos = {(2, 2), (2, 3), (2, 4), (2, 5), (3, 2), (3, 3), (3, 4), (3, 5), (4, 2), (4, 3), (4, 4), (4, 5),
                      (5, 2), (5, 3), (5, 4), (5, 5)}
        ordered_list = []
        count = 0
        for move, value in list:
            if self.is_quite_move(move, value) == 0:
                ordered_list.insert(0, (move, value))
                count += 1
            elif value in middle_pos:
                ordered_list.insert(count, (move, value))
            else:
                ordered_list.append((move, value))

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

    def is_quite_move(self, node, ismax, seq, dest):  # Check if the move is quite
        if ismax:
            if node[dest[0]][dest[1]] <= -300 or self.move_generator.is_king_threatened(seq, dest, not ismax, node):
                return 0
        elif not ismax:
            if node[dest[0]][dest[1]] >= 300 or self.move_generator.is_king_threatened(seq, dest, not ismax, node):
                return 0

        return 1

    def quite_search(self, node, depth, alpha, beta, is_max, path):  # Quiescence search
        if is_max:
            best_value = alpha
            best_path = path
            for child_move, child_value, in self.generate_child_node_without_castling(node, is_max):
                if not self.is_quite_move(node, is_max, child_move, child_value):
                    #print("Not a quite move")
                    child_board = np.copy(node)
                    self.move_piece_alphabeta(child_move, child_value, child_board, True)  # Update the board with the move
                    value = self.eval.board_evaluation(child_board, self.move_count)
                    if value > best_value:
                        best_value = value
                        best_path = path + [(child_move, child_value)]
                    if best_value >= beta:  # Beta-Cutoff
                        break
            #print("Returned:", best_value, best_path)
            return best_value, best_path
        else:
            best_value = beta
            best_path = path
            for child_move, child_value in self.generate_child_node_without_castling(node, is_max):
                if not self.is_quite_move(node, is_max, child_move, child_value):
                    print("Not a quit move")
                    child_board = np.copy(node)
                    self.move_piece_alphabeta(child_move, child_value, child_board, False)  # Update the board with the move
                    value = self.eval.board_evaluation(child_board, self.move_count)
                    if value < best_value:
                        best_value = value
                        best_path = path + [(child_move, child_value)]
                    if best_value <= alpha:  # Alpha-Cutoff
                        break
            #print("Returned:", best_value, best_path)
            return best_value, best_path

    def alpha_beta_hashing(self, node, depth, alpha, beta, is_max, path=[]):
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
            for child_move, child_value, in self.zugsortierung(node,is_max):
                child_board = np.copy(node)
                self.move_piece_alphabeta(child_move, child_value, child_board, True) # Update the board with the move

                value, child_path = self.alpha_beta_hashing(child_board, depth - 1, best_value, beta, False, path + [(child_move, child_value)])
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
            for child_move, child_value in self.zugsortierung(node,is_max):
                child_board = np.copy(node)
                self.move_piece_alphabeta(child_move, child_value, child_board, False)# Update the board with the move

                value, child_path = self.alpha_beta_hashing(child_board, depth - 1, alpha, best_value, True,
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
        return child_node_list
    def generate_child_node_without_castling(self, node,isMax):
        child_node_list = []
        if isMax:
            positions = np.where(node > 0)
            move_dict = self.move_generator.legalMovesWithoutCastling(node, positions, isMax)
        else:
            positions = np.where(node < 0)
            move_dict = self.move_generator.legalMovesWithoutCastling(node, positions,isMax)
        for key, value_list in move_dict.items():
            for value in value_list:
                child_node_list.append((key, value))  # Store the move and resulting board
        return child_node_list

    def alpha_beta(self, node, depth, alpha, beta, is_max, path=[]):
        if depth == 0 or self.gameOver(node,is_max):
            return self.eval.board_evaluation(node,self.move_count), path
        if is_max:
            best_value = alpha
            best_path = None
            for child_move, child_value, in self.generate_child_node(node,is_max):
                child_board = np.copy(node)
                self.move_piece_alphabeta(child_move, child_value, child_board, True) # Update the board with the move

                value, child_path = self.alpha_beta(child_board, depth - 1, best_value, beta, False, path + [(child_move, child_value)])
                if value > best_value:
                    best_value = value
                    best_path = child_path
                if best_value >= beta:  # Beta-Cutoff
                    break
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
            return best_value, best_path

    def alpha_beta_without_castling(self, node, depth, alpha, beta, is_max, path=[]):
        if self.gameOver(node, is_max):
            return self.eval.board_evaluation(node, self.move_count), path
        if depth == 0:
            # Quiescence search
            value, child_path = self.quite_search(node, depth, alpha, beta, is_max, path)
            if value == float('inf') or value == float('-inf'):
                value = self.eval.board_evaluation(node, self.move_count)
                return value, child_path
            return value, child_path
        """if depth == 0 or self.gameOver(node, is_max):
            return self.eval.board_evaluation(node, self.move_count), path"""
        if is_max:
            best_value = alpha
            best_path = None
            for child_move, child_value, in self.generate_child_node_without_castling(node, is_max):
                child_board = np.copy(node)
                self.move_piece_alphabeta(child_move, child_value, child_board, True)  # Update the board with the move
                value, child_path = self.alpha_beta_without_castling(child_board, depth - 1, best_value, beta, False,
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
            for child_move, child_value in self.generate_child_node_without_castling(node, is_max):
                child_board = np.copy(node)
                self.move_piece_alphabeta(child_move, child_value, child_board, False)  # Update the board with the move
                value, child_path = self.alpha_beta_without_castling(child_board, depth - 1, alpha, best_value, True,
                                                                path + [(child_move, child_value)])
                if value < best_value:
                    best_value = value
                    best_path = child_path
                if best_value <= alpha:  # Alpha-Cutoff
                    break
            return best_value, best_path
    def bot_plays(self, algorithm):
        if algorithm == "alphabeta":
            _, path = self.alpha_beta_without_castling(self.chessBoard, 3, float("-inf"), float("inf"), self.isMax)
            if path is None or len(path) == 0:
                self.last_condition = "defeat"
                self.urgency = True
                return -1
            move = path[0]
            sqSelected, sqDest = move
            print(sqSelected)
            self.move_piece(sqSelected, sqDest, self.chessBoard)
            return sqSelected, sqDest
        elif algorithm == "montecarlo":
            best_node = bot_play_monte_carlo(self.chessBoard, self.isMax, self.move_count, 200)
            if best_node == 0:
                self.last_condition = "defeat"
                self.urgency = True
                return -1
            last_move = np.transpose(np.where(self.chessBoard != best_node.move))
            self.last_move = last_move
            move = best_node.move
            self.chessBoard = move
            self.isMax = not self.isMax
            self.move_count += 1
            return 1

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
          moves = self.move_generator.legalMovesWithoutCastling(board, positions, isMax)
          if all(element == [] for element in list(moves.values())):
             return True
        else:
            positions = np.where(board < 0)
            moves = self.move_generator.legalMovesWithoutCastling(board, positions, isMax)
            if all(element == [] for element in list(moves.values())):
                return True
        return False






























