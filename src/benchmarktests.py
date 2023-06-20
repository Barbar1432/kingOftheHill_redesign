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
    board, color, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (
    enPassentSquareRow, enPassentSquareCol), halfMoveClock, fullMoveClock = FENtoBoard(board2)
    a_b_board_1.chessBoard = board
    a_b_board_1.can_castle_black_right = kingsideCastleBlack
    a_b_board_1.can_castle_black_left = queensideCastleBlack
    a_b_board_1.can_castle_white_right = kingsideCastleWhite
    a_b_board_1.can_castle_white_left = queensideCastleWhite
    if color == 'black':
        a_b_board_1.isMax = False
    move_generator = moveGenerator()
    _, path, k = a_b_board_1.alpha_beta_count(a_b_board_1.chessBoard, 1, float("-inf"), float("inf"), a_b_board_1.isMax)

    move = path[0]

    print("AlphaBeta depth 1 untersuchter Zustände: ", k)
    print("Best Move Found: ", move)



def alpha_beta_depth2():
    a_b_board_2 = Board()
    board, color, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (
        enPassentSquareRow, enPassentSquareCol), halfMoveClock, fullMoveClock = FENtoBoard(board2)
    a_b_board_2.chessBoard = board
    a_b_board_2.can_castle_black_right = kingsideCastleBlack
    a_b_board_2.can_castle_black_left = queensideCastleBlack
    a_b_board_2.can_castle_white_right = kingsideCastleWhite
    a_b_board_2.can_castle_white_left = queensideCastleWhite
    if color == 'black':
        a_b_board_2.isMax = False
    move_generator = moveGenerator()
    _, path, k = a_b_board_2.alpha_beta_count(a_b_board_2.chessBoard, 2, float("-inf"), float("inf"), a_b_board_2.isMax)

    move = path[0]

    print("AlphaBeta depth 2 untersuchter Zustände: ", k)
    print("Best Move Found: ", move)

def alpha_beta_depth3():
    a_b_board_3 = Board()
    board, color, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (
        enPassentSquareRow, enPassentSquareCol), halfMoveClock, fullMoveClock = FENtoBoard(board2)
    a_b_board_3.chessBoard = board
    a_b_board_3.can_castle_black_right = kingsideCastleBlack
    a_b_board_3.can_castle_black_left = queensideCastleBlack
    a_b_board_3.can_castle_white_right = kingsideCastleWhite
    a_b_board_3.can_castle_white_left = queensideCastleWhite
    if color == 'black':
        a_b_board_3.isMax = False

    _, path, k = a_b_board_3.alpha_beta_count(a_b_board_3.chessBoard, 3, float("-inf"), float("inf"), a_b_board_3.isMax)

    move = path[0]

    print("AlphaBeta depth 3 untersuchter Zustände: ", k)
    print("Best Move Found: ", move)

def alpha_beta_depth4():
    a_b_board_4 = Board()
    board, color, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (
        enPassentSquareRow, enPassentSquareCol), halfMoveClock, fullMoveClock = FENtoBoard(board2)
    a_b_board_4.chessBoard = board
    a_b_board_4.can_castle_black_right = kingsideCastleBlack
    a_b_board_4.can_castle_black_left = queensideCastleBlack
    a_b_board_4.can_castle_white_right = kingsideCastleWhite
    a_b_board_4.can_castle_white_left = queensideCastleWhite
    if color == 'black':
        a_b_board_4.isMax = False

    _, path, k = a_b_board_4.alpha_beta_count(a_b_board_4.chessBoard, 4, float("-inf"), float("inf"), a_b_board_4.isMax)

    move = path[0]

    print("AlphaBeta depth 3 untersuchter Zustände: ", k)
    print("Best Move Found: ", move)

"""
def min_max_depth1():
    min_max_1 = Board()
    board, color, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (
        enPassentSquareRow, enPassentSquareCol), halfMoveClock, fullMoveClock = FENtoBoard(board1)
    min_max_1.chessBoard = board
    min_max_1.can_castle_black_right = kingsideCastleBlack
    min_max_1.can_castle_black_left = queensideCastleBlack
    min_max_1.can_castle_white_right = kingsideCastleWhite
    min_max_1.can_castle_white_left = queensideCastleWhite
    if color == 'black':
        min_max_1.isMax = False

    _, path, k = min_max_1.min_max_count(min_max_1.chessBoard, 1, float('-inf'), float('inf'), min_max_1.isMax)

    move = path[0]

    print("MinMax depth 1 untersuchter Zustände: ", k)
    print("Best Move Found: ", move)


def min_max_depth2():
    min_max_2 = Board()
    board, color, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (
        enPassentSquareRow, enPassentSquareCol), halfMoveClock, fullMoveClock = FENtoBoard(board1)
    min_max_2.chessBoard = board
    min_max_2.can_castle_black_right = kingsideCastleBlack
    min_max_2.can_castle_black_left = queensideCastleBlack
    min_max_2.can_castle_white_right = kingsideCastleWhite
    min_max_2.can_castle_white_left = queensideCastleWhite
    if color == 'black':
        min_max_2.isMax = False

    _, path, k = min_max_2.min_max_count(min_max_2.chessBoard, 2, float('-inf'), float('inf'), min_max_2.isMax)

    move = path[0]

    print("MinMax depth 2 untersuchter Zustände: ", k)
    print("Best Move Found: ", move)


def min_max_depth3():
    min_max_3 = Board()
    board, color, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (
        enPassentSquareRow, enPassentSquareCol), halfMoveClock, fullMoveClock = FENtoBoard(board1)
    min_max_3.chessBoard = board
    min_max_3.can_castle_black_right = kingsideCastleBlack
    min_max_3.can_castle_black_left = queensideCastleBlack
    min_max_3.can_castle_white_right = kingsideCastleWhite
    min_max_3.can_castle_white_left = queensideCastleWhite
    if color == 'black':
        min_max_3.isMax = False

    _, path, k = min_max_3.min_max_count(min_max_3.chessBoard, 3, float('-inf'), float('inf'), min_max_3.isMax)

    move = path[0]

    print("MinMax depth 3 untersuchter Zustände: ", k)
    print("Best Move Found: ", move)
"""
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
    array6 = (
        timeit.repeat(stmt='alpha_beta_depth1()', setup='from __main__ import alpha_beta_depth1', repeat=5, number=1))
    #array11 = (
    #    timeit.repeat(stmt='min_max_depth1()', setup='from __main__ import min_max_depth1', repeat=1, number=1))
    array1 = (
        timeit.repeat(stmt='alpha_beta_depth1()', setup='from __main__ import alpha_beta_depth1', repeat=5, number=1))
    #array22 = (
    #    timeit.repeat(stmt='min_max_depth2()', setup='from __main__ import min_max_depth2', repeat=1, number=1))
    array2 = (
        timeit.repeat(stmt='alpha_beta_depth2()', setup='from __main__ import alpha_beta_depth2', repeat=5, number=1))
    #array33 = (
    #    timeit.repeat(stmt='min_max_depth3()', setup='from __main__ import min_max_depth3', repeat=1, number=1))
    array3 = (
        timeit.repeat(stmt='alpha_beta_depth3()', setup='from __main__ import alpha_beta_depth3', repeat=5, number=1))
    array4 = (
        timeit.repeat(stmt='alpha_beta_depth4()', setup='from __main__ import alpha_beta_depth4', repeat=5, number=1))

    x = range(1, 6)
    # With Min-Max:
    """fig, axs = plt.subplots(3, 2)
    axs[0, 0].plot(x, array11, 'tab:blue')
    axs[0, 0].set_title('MinMax with Depth: 1')
    axs[0, 0].set_ylabel('time (s)')
    axs[0, 1].plot(x, array1, 'tab:cyan')
    axs[0, 1].set_title('AlphaBeta with Depth: 1')
    axs[1, 0].plot(x, array22, 'tab:red')
    axs[1, 0].set_title('MinMax with Depth: 2')
    axs[1, 0].set_ylabel('time (s)')
    axs[1, 1].plot(x, array2, 'tab:orange')
    axs[1, 1].set_title('AlphaBeta with Depth: 2')
    axs[2, 0].plot(x, array33, 'tab:purple')
    axs[2, 0].set_title('MinMax with Depth: 3')
    axs[2, 0].set_ylabel('time (s)')
    axs[2, 0].set_xlabel('repeat (n)')
    axs[2, 1].plot(x, array3, 'tab:pink')
    axs[2, 1].set_title('AlphaBeta with Depth: 3')
    axs[2, 1].set_xlabel('repeat(n)')
    fig.tight_layout()
    plt.show()"""
    # Without Min-Max:
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot(x, array1)
    axs[0, 0].set_title('AlphaBeta with Depth: 1')
    axs[0, 0].set_ylabel('time (s)')
    axs[0, 1].plot(x, array2, 'tab:green')
    axs[0, 1].set_title('AlphaBeta with Depth: 2')
    axs[1, 0].plot(x, array3, 'tab:red')
    axs[1, 0].set_title('AlphaBeta with Depth: 3')
    axs[1, 0].set_ylabel('time (s)')
    axs[1, 0].set_xlabel('repeat (n)')
    axs[1, 1].plot(x, array4, 'tab:purple')
    axs[1, 1].set_title('AlphaBeta with Depth: 4')
    axs[1, 1].set_xlabel('repeat (n)')
    fig.tight_layout()
    plt.show()