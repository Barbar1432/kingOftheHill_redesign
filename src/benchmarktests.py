import timeit
import time
import matplotlib.pyplot as plt
import numpy as np
import random
from board import Board
from tests import FENtoBoard
from moveGenerator import moveGenerator

testing = 1 # 0 for Zuggenerator , 1 for MinMax - AlphaBetaSuche
board1 = "4k2r/r2n1pbp/3B2p1/p1p3P1/2p4P/7B/PP2K3/1R4NR w k - 0 22"
board2 = "r1b1k1nr/1pp2ppp/p1p5/2b1p3/P3P3/2N2PP1/1PPP3q/R1B1KQ2 w Qkq - 0 11"
board3 = "8/2p2R2/1p2p1Np/1P5k/3nr3/8/P7/2K5 w - - 0 34"

def randomizer(moves_list):
    return random.choice(moves_list)

def zug_generator_starting():
    boardd = Board()
    positions = np.where(boardd.chessBoard > 0)
    can_castle_left = boardd.can_castle_white_left
    can_castle_right = boardd.can_castle_white_right
    move_generator = moveGenerator()
    moves = move_generator.legalMoves(boardd.chessBoard, positions, boardd.isMax, can_castle_right, can_castle_left)
    list_of_possible_moves = []
    row_indices, col_indices = positions
    for row, col in zip(row_indices, col_indices):
        pos = (row, col)
        legal_moves = moves[pos]
        while len(legal_moves) != 0:
            move = legal_moves.pop()
            possible_move = (pos, move)
            list_of_possible_moves.append(possible_move)

    move = randomizer(list_of_possible_moves)
def zug_generator_middle():
    boardmiddle = Board()
    boardmid_d, color, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (enPassentSquareRow, enPassentSquareCol), \
        halfMoveClock, fullMoveClock = FENtoBoard("4k2r/r2n1pbp/3B2p1/p1p3P1/2p4P/7B/PP2K3/1R4NR w k - 0 22")
    boardmiddle.chessBoard = boardmid_d
    boardmiddle.can_castle_black_right = kingsideCastleBlack
    boardmiddle.can_castle_black_left = queensideCastleBlack
    boardmiddle.can_castle_white_right = kingsideCastleWhite
    boardmiddle.can_castle_white_left = queensideCastleWhite
    if color == 'black':
        boardmiddle.isMax = False
    move_generator = moveGenerator()
    if color == 'white':
        positions = np.where(boardmiddle.chessBoard > 0)
        can_castle_left = boardmiddle.can_castle_white_left
        can_castle_right = boardmiddle.can_castle_white_right
    else:
        positions = np.where(boardmiddle.chessBoard < 0)
        can_castle_left = boardmiddle.can_castle_black_left
        can_castle_right = boardmiddle.can_castle_black_right
    list_of_possible_moves = []
    moves = move_generator.legalMoves(boardmiddle.chessBoard, positions, boardmiddle.isMax, can_castle_right, can_castle_left)
    row_indices, col_indices = positions
    for row, col in zip(row_indices, col_indices):
        pos = (row, col)
        legal_moves = moves[pos]
        while len(legal_moves) != 0:
            move = legal_moves.pop()
            possible_move = (pos, move)
            list_of_possible_moves.append(possible_move)

    move = randomizer(list_of_possible_moves)

def zug_generator_end():
    boardend = Board()
    boardend_d, color, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (enPassentSquareRow, enPassentSquareCol), \
        halfMoveClock, fullMoveClock = FENtoBoard("r1b1k1nr/1pp2ppp/p1p5/2b1p3/P3P3/2N2PP1/1PPP3q/R1B1KQ2 w Qkq - 0 11")
    #print(boardmid, color)
    boardend.chessBoard = boardend_d
    boardend.can_castle_black_right = kingsideCastleBlack
    boardend.can_castle_black_left = queensideCastleBlack
    boardend.can_castle_white_right = kingsideCastleWhite
    boardend.can_castle_white_left = queensideCastleWhite
    if color == 'black':
        boardend.isMax = False
    move_generator = moveGenerator()
    if color == 'white':
        positions = np.where(boardend.chessBoard > 0)
        can_castle_left = boardend.can_castle_white_left
        can_castle_right = boardend.can_castle_white_right
    else:
        positions = np.where(boardend.chessBoard < 0)
        can_castle_left = boardend.can_castle_black_left
        can_castle_right = boardend.can_castle_black_right
    list_of_possible_moves = []
    moves = move_generator.legalMoves(boardend.chessBoard, positions, boardend.isMax, can_castle_right, can_castle_left)
    row_indices, col_indices = positions
    for row, col in zip(row_indices, col_indices):
        pos = (row, col)
        legal_moves = moves[pos]
        while len(legal_moves) != 0:
            move = legal_moves.pop()
            possible_move = (pos, move)
            list_of_possible_moves.append(possible_move)

    move = randomizer(list_of_possible_moves)

def alpha_beta_depth1():
    a_b_board_1 = Board()
    board_d, color, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (enPassentSquareRow, enPassentSquareCol), \
    halfMoveClock, fullMoveClock= FENtoBoard(board2)
    a_b_board_1.chessBoard = board_d
    a_b_board_1.can_castle_black_left = queensideCastleBlack
    a_b_board_1.can_castle_black_right = kingsideCastleBlack
    a_b_board_1.can_castle_white_left = queensideCastleWhite
    a_b_board_1.can_castle_white_right = kingsideCastleWhite
    if color == 'black':
        a_b_board_1.isMax = False
    bewertung, path, k = a_b_board_1.alpha_beta_count(a_b_board_1.chessBoard, 1, float('-inf'), float('inf'), True)
    move = path[0]

    print("AlphaBeta depth 1 untersuchter Zustände: ", k)

def alpha_beta_depth2():
    a_b_board_2 = Board()
    board_d, color, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (
    enPassentSquareRow, enPassentSquareCol), \
        halfMoveClock, fullMoveClock = FENtoBoard(board2)
    a_b_board_2.chessBoard = board_d
    a_b_board_2.can_castle_black_left = queensideCastleBlack
    a_b_board_2.can_castle_black_right = kingsideCastleBlack
    a_b_board_2.can_castle_white_left = queensideCastleWhite
    a_b_board_2.can_castle_white_right = kingsideCastleWhite
    if color == 'black':
        a_b_board_2.isMax = False
    bewertung, path, k = a_b_board_2.alpha_beta_count(a_b_board_2.chessBoard, 2, float('-inf'), float('inf'), True)
    move = path[0]
    print("AlphaBeta depth 2 untersuchter Zustände: ", k)
def alpha_beta_depth3():
    a_b_board_3 = Board()
    board_d, color, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (
    enPassentSquareRow, enPassentSquareCol), \
        halfMoveClock, fullMoveClock = FENtoBoard(board2)
    a_b_board_3.chessBoard = board_d
    a_b_board_3.can_castle_black_left = queensideCastleBlack
    a_b_board_3.can_castle_black_right = kingsideCastleBlack
    a_b_board_3.can_castle_white_left = queensideCastleWhite
    a_b_board_3.can_castle_white_right = kingsideCastleWhite
    if color == 'black':
        a_b_board_3.isMax = False
    bewertung, path, k = a_b_board_3.alpha_beta_count(a_b_board_3.chessBoard, 3, float('-inf'), float('inf'), True)
    move = path[0]
    print("AlphaBeta depth 3 untersuchter Zustände: ", k)

def alpha_beta_depth1q():
    a_b_board_1 = Board()
    board_d, color, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (enPassentSquareRow, enPassentSquareCol), \
    halfMoveClock, fullMoveClock, = FENtoBoard(board2)
    a_b_board_1.chessBoard = board_d
    a_b_board_1.can_castle_black_left = queensideCastleBlack
    a_b_board_1.can_castle_black_right = kingsideCastleBlack
    a_b_board_1.can_castle_white_left = queensideCastleWhite
    a_b_board_1.can_castle_white_right = kingsideCastleWhite
    if color == 'black':
        a_b_board_1.isMax = False
    bewertung, path, k = a_b_board_1.alpha_beta_with_quite_search_count(a_b_board_1.chessBoard, 1, float('-inf'), float('inf'), True)
    move = path[0]

    print("AlphaBeta depth 1 untersuchter Zustände: ", k)

def alpha_beta_depth2q():
    a_b_board_2 = Board()
    board_d, color, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (
    enPassentSquareRow, enPassentSquareCol), \
        halfMoveClock, fullMoveClock = FENtoBoard(board2)
    a_b_board_2.chessBoard = board_d
    a_b_board_2.can_castle_black_left = queensideCastleBlack
    a_b_board_2.can_castle_black_right = kingsideCastleBlack
    a_b_board_2.can_castle_white_left = queensideCastleWhite
    a_b_board_2.can_castle_white_right = kingsideCastleWhite
    if color == 'black':
        a_b_board_2.isMax = False
    bewertung, path, k = a_b_board_2.alpha_beta_with_quite_search_count(a_b_board_2.chessBoard, 2, float('-inf'), float('inf'), True)
    move = path[0]
    print("AlphaBeta depth 2 untersuchter Zustände: ", k)
def alpha_beta_depth3q():
    a_b_board_3 = Board()
    board_d, color, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (
    enPassentSquareRow, enPassentSquareCol), \
        halfMoveClock, fullMoveClock = FENtoBoard(board2)
    a_b_board_3.chessBoard = board_d
    a_b_board_3.can_castle_black_left = queensideCastleBlack
    a_b_board_3.can_castle_black_right = kingsideCastleBlack
    a_b_board_3.can_castle_white_left = queensideCastleWhite
    a_b_board_3.can_castle_white_right = kingsideCastleWhite
    if color == 'black':
        a_b_board_3.isMax = False
    bewertung, path, k = a_b_board_3.alpha_beta_with_quite_search_count(a_b_board_3.chessBoard, 3, float('-inf'), float('inf'), True)
    move = path[0]
    print("AlphaBeta depth 3 untersuchter Zustände: ", k)

if (testing == 0):
    array1 = (
        timeit.repeat(stmt='zug_generator_starting()', setup='from __main__ import zug_generator_starting', repeat=5,
                      number=1))
    array4 = (
        timeit.repeat(stmt='zug_generator_starting()', setup='from __main__ import zug_generator_starting', repeat=1000,
                      number=1))
    array2 = (
        timeit.repeat(stmt='zug_generator_middle()', setup='from __main__ import zug_generator_middle', repeat=1000,
                      number=1))
    array3 = timeit.repeat(stmt='zug_generator_end()', setup='from __main__ import zug_generator_end', repeat=1000,
                           number=1)
    x = range(1, 1001)
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot(x, array4)
    axs[0, 0].set_title('Starting board')
    axs[0, 1].plot(x, array2, 'tab:green')
    axs[0, 1].set_title('Middle board')
    axs[1, 0].plot(x, array3, 'tab:red')
    axs[1, 0].set_title('Near-end board')
    fig.tight_layout()
    plt.yticks([0.0, 0.1, 0.2, 0.3, 0.4])
    plt.show()

elif testing == 1:
    array4 = (
        timeit.repeat(stmt='alpha_beta_depth1()', setup='from __main__ import alpha_beta_depth1', repeat=5, number=1))
    array1 = (
        timeit.repeat(stmt='alpha_beta_depth1()', setup='from __main__ import alpha_beta_depth1', repeat=10, number=1))
    array2 = (
        timeit.repeat(stmt='alpha_beta_depth2()', setup='from __main__ import alpha_beta_depth2', repeat=10, number=1))
    array3 = (
        timeit.repeat(stmt='alpha_beta_depth3()', setup='from __main__ import alpha_beta_depth3', repeat=10, number=1))
    """array11 = (
        timeit.repeat(stmt='alpha_beta_depth1q()', setup='from __main__ import alpha_beta_depth1q', repeat=3, number=1))
    array22 = (
        timeit.repeat(stmt='alpha_beta_depth2q()', setup='from __main__ import alpha_beta_depth2q', repeat=3, number=1))
    array33 = (
        timeit.repeat(stmt='alpha_beta_depth3q()', setup='from __main__ import alpha_beta_depth3q', repeat=3, number=1))
    """

    x = range(1, 11)
    fig, axs = plt.subplots(3, 2)
    axs[0, 0].plot(x, array1, 'tab:cyan')
    axs[0, 0].set_title('AlphaBeta with Depth: 1')
    axs[0, 0].set_ylabel('time (s)')
    """axs[0, 1].plot(x, array11, 'tab:cyan')
    axs[0, 1].set_title('AlphaBeta with Quite Search Depth: 1')"""
    axs[1, 0].plot(x, array2, 'tab:orange')
    axs[1, 0].set_title('AlphaBeta with Depth: 2')
    axs[1, 0].set_ylabel('time (s)')
    """axs[1, 1].plot(x, array22, 'tab:orange')
    axs[1, 1].set_title('AlphaBeta with Quite Search Depth: 2')"""
    axs[2, 0].plot(x, array3, 'tab:pink')
    axs[2, 0].set_title('AlphaBeta with Depth: 3')
    axs[2, 0].set_ylabel('time (s)')
    axs[2, 0].set_xlabel('repeat (n)')
    """axs[2, 1].plot(x, array33, 'tab:pink')
    axs[2, 1].set_title('AlphaBeta with Quite Search Depth: 3')"""
    axs[2, 1].set_xlabel('repeat(n)')
    fig.tight_layout()
    plt.show()




# Count Functions - For testing add these in class Board():
"""
    def quite_search_count(self, node, depth, alpha, beta, is_max, k, path):  # Quiescence search
        k += 1
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
            return best_value, best_path, k

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
            return best_value, best_path, k

    def alpha_beta(self, node, depth, alpha, beta, is_max, k=0, path=[]):
        originalAlpha = alpha

        hash_key = self.board_hash(node)
        if hash_key in transposition_table:

            entry = transposition_table[hash_key]
            if entry['depth'] >= depth:
                if entry['flag'] == 'exact':

                    return entry['value'], entry['path'], k

                elif entry['flag'] == 'lowerbound':
                    alpha = max(alpha, entry['value'])
                elif entry['flag'] == 'upperbound':
                    beta = min(beta, entry['value'])
                if alpha >= beta:
                    return entry['value'], entry['path'], k
        k += 1
        if self.gameOver(node, is_max):
            return self.eval.board_evaluation(node,self.move_count), path, k
        if depth == 0:
            # Quiescence search
            value, child_path, k = self.quite_search(node, depth, alpha, beta, is_max, k, path)
            return value, child_path, k
        if is_max:
            best_value = alpha
            best_path = None
            for child_move, child_value, in self.generate_child_node(node,is_max):
                child_board = np.copy(node)
                self.move_piece_alphabeta(child_move, child_value, child_board, True) # Update the board with the move

                value, child_path, k = self.alpha_beta(child_board, depth - 1, best_value, beta, False, k, path + [(child_move, child_value)])
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
            return best_value, best_path, k
        else:
            best_value = beta
            best_path = None
            for child_move, child_value in self.generate_child_node(node,is_max):
                child_board = np.copy(node)
                self.move_piece_alphabeta(child_move, child_value, child_board, False)# Update the board with the move

                value, child_path, k = self.alpha_beta(child_board, depth - 1, alpha, best_value, True, k,
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
            return best_value, best_path, k
"""

